function CityDigitsMap() {
    //init values
    this.closeTooltip = null;
    this.neighborhoodLayer = null;

    //load map
//    var basemap = "sw2279.NYCLotto";
    var basemap = "sw2279.map-x3k7qi26";

    //where brooklyn at?!40.7429 N, 73.9188
    this.map = L.mapbox.map('map', basemap).setView([40.7429,-73.9188], 13);;
    //set params
    this.height = $(window).height()-$(".navbar").height();
    this.width = $(window).width();

     //disable unwanted events
    this.map.touchZoom.disable();
    this.map.doubleClickZoom.disable();
    this.map.scrollWheelZoom.disable();
    this.map.gridControl.options.follow = true;

    this.popup = new L.Popup({ autoPan: false });

}

//CityDigitsMap.prototype.onEachFeature = function(feature, layer) {
//    console.log("ON EACH FEATURE");
////       );
//}


CityDigitsMap.prototype.loadLayers =  function (){
    var self = this;
    console.log("LOADING LAYERS");
    //show map ui nav
    $("#map-nav").load("/map/nav/");

    //add neighborhoods
    this.neighborhoodLayer = L.geoJson(nyc_neighborhoods,{
        style :CityDigitsMap.getStyleColorForPercentIncome
    }).addTo(this.map);
    this.neighborhoodLayer.on('mouseover', function(e) {
        self.mapMouseMove(e);
    });
    this.neighborhoodLayer.on('mouseout', function(e) {
        self.mapMouseOut(e);
    });
    this.neighborhoodLayer.on('click', function(e) {
        self.mapMouseMove(e);
        //load popup
        showMapPopUp(e);
    });
}

CityDigitsMap.prototype.resizeMap = function(){
    $("#map").height(this.height);
    $("#map").width(this.width);
}

CityDigitsMap.prototype.mapMouseMove = function (ev){
    //get layer
    var layer = ev.layer;

    //verify feature
    if(layer.feature != undefined){
            //get lat/long
        this.popup.setLatLng(ev.latlng);
        this.popup.setContent(layer.feature.properties.N_Name);
        //display popup
        if (!this.popup._map) this.popup.openOn(this.map);
        window.clearTimeout(this.closeTooltip);
    }
    return false;
}

CityDigitsMap.prototype.mapMouseOut = function(e) {
    var self = this;
//    this.neighborhoodLayer.resetStyle(e.target);
//    this.closeTooltip = window.setTimeout(function() {
//        self.map.closePopup();
//        }, 100);
}

CityDigitsMap.getStyleColorForPercentIncome = function (feature){
//    fillColor = "#FFFFFF";
    try{
        var percent = feature.properties.PERINC10;
        var fillColor = null;
        if(percent >= 0 && percent <=.5){
            fillColor =  "#b2eaee";
        }
        if(percent >.5 && percent <=1.5){
            fillColor =  "#79CADA";
        }
        if(percent >1.5 && percent<=2){
            fillColor = "#42B7BD";
        }
        if(percent > 2 && percent <=3){
            fillColor =  "#4794D4";
        }
        if(percent > 3 && percent <=15){
            fillColor =  "#526CD9";
        }
    }catch (e){

    }finally{
        return {
        weight: 2,
        opacity: 0.1,
        color: 'black',
        fillOpacity: 0.75,
        fillColor: fillColor
        }
    }
}

CityDigitsMap.getStyleColorForMedianIncome = function (feature){
    var income = feature.properties.Daily_Inco;
    var fillColor = null;
    if(income >= 0 && income <=100){
        fillColor =  "#D2F7F0";
    }
    if(income >100 && income <=140){
        fillColor =  "#8DEFE3";
    }
    if(income >140 && income<=170){
        fillColor = "#28E5E0";
    }
    if(income > 170 && income <=220){
        fillColor = "#00C9C8";
    }
    if(income > 220 && income <=450){
        fillColor = "#00A1B7";
    }

     return {
         weight: 2,
         opacity: 0.1,
         color: 'black',
         fillOpacity: 0.75,
         fillColor: fillColor
    }
}

CityDigitsMap.getStyleColorForAverageWin = function(feature){
    var winnings = feature.properties.Daily_Win;
    var fillColor = null;
    if(winnings >= 0 && winnings <=30){
        fillColor =  "#E7D6FC";
    }
    if(winnings >30 && winnings <=60){
        fillColor =  "#DDA4FC";
    }
    if(winnings >60 && winnings<=90){
        fillColor = "#CA6BF2";
    }
    if(winnings > 90 && winnings <=130){
        fillColor = "#9518ED";
    }
    if(winnings > 130 && winnings <=2700){
        fillColor = "#6122FC";
    }

     return {
         weight: 2,
         opacity: 0.1,
         color: 'black',
         fillOpacity: 0.75,
         fillColor: fillColor
    }

}

CityDigitsMap.getStyleColorForAverageSpend = function(feature){
    var spent = feature.properties.Daily_Sale;
    var fillColor = null;
    if(spent >= 0 && spent <=800){
        fillColor =  "#EEFC9C";
    }
    if(spent >800 && spent <=1070){
        fillColor =  "#B0FC95";
    }
    if(spent >1070 && spent<=1280){
        fillColor = "#60FD7C";
    }
    if(spent > 1280 && spent <=1630){
        fillColor = "#00EC66";
    }
    if(spent > 1630 && spent <=8000){
        fillColor = "#00B95C";
    }

     return {
         weight: 2,
         opacity: 0.1,
         color: 'black',
         fillOpacity:.75,
         fillColor: fillColor
    }

}

CityDigitsMap.getStyleColorForNetWinLoss = function(feature){
    var net = feature.properties.Net_Win;
    var fillColor = null;
    if(net >= -6700 && net <=-1500){
        fillColor =  "#BF46B1";
    }
    if(net >-1500 && net <=-1200){
        fillColor =  "#E1DBC8";
    }
    if(net >-1200 && net<=-1000){
        fillColor = "#DE88C8";
    }
    if(net > -1000 && net <=0){
        fillColor = "#E5AFD8";
    }
    if(net > 0 && net <=1300){
        fillColor = "#EECAE5";
    }

     return {
         weight: 2,
         opacity: 0.1,
         color: 'black',
         fillOpacity: 0.75,
         fillColor: fillColor
    }

}
