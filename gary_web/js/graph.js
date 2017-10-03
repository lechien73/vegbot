// For responsiveness that doesn't break on an iPad

var windowWidth = ($(window).width());

window.onresize = function() {
	if (windowWidth !== ($(window).width())) {
    	location.reload();
    }
}

d3.csv("../counter.log", function(error, projectsCSV) {
    console.log(error);
    var keywordArray = [];
    var garyData = projectsCSV;
    var dateFormat = d3.time.format("%Y-%m-%d");
    garyData.forEach(function (d) {
        d["date"] = dateFormat.parse(d["date"]);
        if(keywordArray.indexOf(d["keyword"]) == -1) {
            keywordArray.push(d["keyword"]);
        }
     });
     keywordArray.sort();

    var dateChartWidth = $("#date-chart").width();
    var dateChartHeight = dateChartWidth / 2;
    var keywordChartWidth = $("#keyword-chart").width();
    var keywordChartHeight = keywordChartWidth / 2;
    var subredditChartWidth = $("#subreddit-pie-chart").width() / 1.5;
    var subredditChartHeight = subredditChartWidth;
    var subredditChartRadius = subredditChartWidth / 2.5;
    var subredditChartInnerRadius = subredditChartRadius / 2;

    var ndx = crossfilter(garyData);

    var dateDim = ndx.dimension(function (d) {
        return d["date"];
    });

    var keywordDim = ndx.dimension(function (d) {
        return d["keyword"];
    });

    var subredditDim = ndx.dimension(function (d) {
        return d["subreddit"];
    })

    var queryByDate = dateDim.group().reduceSum(function (d) {
        return d["count"];
    });

    var keywordCount = keywordDim.group().reduceSum(function (d) {
        return d["count"];
    });

    var subredditCount = subredditDim.group().reduceSum(function (d) {
        return d["count"];
    });

    var totalQueries = ndx.groupAll().reduceSum(function (d) {
        return d["count"];
    });

    var minDate = dateDim.bottom(1)[0]["date"];
    var maxDate = dateDim.top(1)[0]["date"];


    var dateChart = dc.lineChart("#date-chart");
    var subredditChart = dc.pieChart("#subreddit-pie-chart");
    var keywordChart = dc.barChart("#keyword-chart");
    var queryCount = dc.numberDisplay("#query-count-display");

    dateChart
        .width(dateChartWidth)
        .height(dateChartHeight)
        .margins({top: 20, right: 20, bottom: 60, left: 30})
        .dimension(dateDim)
        .group(queryByDate)
        .transitionDuration(500)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .elasticY(true)
        .xAxisLabel("Date")
        .yAxisLabel("Queries")
        .renderHorizontalGridLines(true)
        .renderVerticalGridLines(true)
        .yAxis().ticks(5);

    subredditChart
        .height(subredditChartHeight)
        .width(subredditChartWidth)
        .radius(subredditChartRadius)
        .innerRadius(subredditChartInnerRadius)
        .transitionDuration(1500)
        .dimension(subredditDim)
        .group(subredditCount);


    keywordChart
        .width(keywordChartWidth)
        .height(keywordChartHeight)
        .margins({top: 20, right: 20, bottom: 80, left: 30})
        .dimension(keywordDim)
        .group(keywordCount)
        .x(d3.scale.ordinal().domain(keywordArray))
        .xAxisLabel("Keywords")
        .yAxisLabel("Queries")
        .xUnits(dc.units.ordinal)
        .xAxis().ticks(5);

    queryCount
        .formatNumber(d3.format("d"))
        .valueAccessor(function (d) {
            return d;
        })
        .group(totalQueries)
        .formatNumber(d3.format("d"));

    dc.renderAll();
});