function buildCharts(sample) {
    d3.json("samples.json").then((data) => {
        var samples = data.samples;
        var filterData = samples.filter(object => object.id == sample);
        var result = filterData[0];

        
        var otu_ids = result.otu_ids;
        var otu_labels = result.otu_labels;
        var sampleValues = result.sample_values;
        

        var barSetup = {
            x: sampleValues.slice(0, 10).reverse(),
            y: otu_ids.slice(0,10).map(newID => `OTU ${newID}`).reverse(),
            text: otu_labels.slice(0, 10).reverse(),
            type: "bar",
            orientation: "h",
        };

        var barData = [barSetup];

        var barLayout = {
            title: "Top Ten OTU's per Sample",
            margin: { t: 50, l: 175} 
        };

        Plotly.newPlot("bar", barData, barLayout);

        var bubbleLayout = {
            title: "Total Bacteria per OTU ID",
            margin: { t:0 },
            hovermode: "closest",
            xaxis: { title: "OTU ID"},
            margin: { t:30}
        };
        var bubbleData = [
            {
                x: otu_ids,
                y: sampleValues,
                text: otu_labels,
                mode: "markers",
                marker: {
                    size: sampleValues,
                    color: otu_ids,
                    colorscale: "Electric"
                }
            }
        ];

        Plotly.newPlot("bubble", bubbleData, bubbleLayout);
    });
}

function buildMetadata(sample) {
    d3.json("samples.json").then((data) => {
        var metaData = data.metadata;
        
        var filterData = metaData.filter(object => object.id == sample);
        var result = filterData[0];
        var panel = d3.select("#sample-metadata");

        panel.html("");

        Object.entries(result).forEach(([key, value]) => {
            panel.append("h6").text(`${key.toUpperCase()}: ${value}`);
        });
    });
}

function init() {
    var select = d3.select("#selDataset");

    d3.json("samples.json").then((data) => {
        var names = data.names;

        names.forEach((sample) => {
            select.append("option").text(sample).property("value", sample);
        });

        var firstSample = names[0];
        buildCharts(firstSample);
        buildMetadata(firstSample);
    });
}

function optionChanged(newSample) {
    buildCharts(newSample);
    buildMetadata(newSample);
}

init();

