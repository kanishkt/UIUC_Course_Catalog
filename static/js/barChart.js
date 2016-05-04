/**
 * Created by kanishk on 5/1/16.
 */
function barcreate(data){
    // myData = ConvertToCSV(file_path)
    console.log(data);
    var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 400 - margin.left - margin.right,
    height = 350 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

  var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<strong></strong> <span style='color:white'>" + d.name+ ", "+parseInt(d.cost) + "%"+"</span>";
  })

jQuery('#barchart').html('');
var svg = d3.select("#barchart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    svg.call(tip);


    //console.log("in here");
  var y_scale = d3.scale.linear()
    .range([0, height]);
  x.domain(data.map(function(d) { return d.name; }));
  y.domain([0, d3.max(data, function(d) { console.log(d.cost);return d.cost; })]);
  y_scale.domain([0, d3.max(data, function(d) { console.log(d.cost);return d.cost; })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .style("font-size", "12px")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", -30)

      .attr("x",-100)
      .style("text-anchor", "end")
      .style("font-size", "12px")
      .text("Percentage Score");

  svg.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide)
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.name); })

      .attr("width", x.rangeBand())
      .attr("y", height)
      .attr("height",0)
      //.attr("height", 0)
      .transition()
      .duration(800)
      .delay(function (d, i) {
        return i * 400;
      })
      .attr("y", function(d) { return height - y_scale(d.cost) })
      .attr("height",function(d) { return y_scale(d.cost); });


  function type(d) {
  d.cost = +d.cost;
  return d;
}
}