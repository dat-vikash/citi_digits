function CityDigitsMap() {
    //init values
    this.closeTooltip = null;
    this.neighborhoodLayer = null;

    //load map
//    var basemap = "sw2279.NYCLotto";
    var basemap = "sw2279.map-x3k7qi26";

    //where brooklyn at?!40.7429 N, 73.9188
    this.map = L.mapbox.map('map', basemap,{minZoom:11,maxZoom:16,zoomControl:false}).setView([40.7429,-73.9188], 13);
    //load zoomer
    $("#citydigits-zoomer").attr({'class':'citydigits-zoomer'});
    $("#citydigits-zoomer").on("click","#zoom-in",CityDigitsMap.onZoomIn);
    $("#citydigits-zoomer").on("click","#zoom-out",CityDigitsMap.onZoomOut);

    //set params
    this.height = $(window).height()-$(".navbar").height();
    this.width = $(window).width();

     //disable unwanted events
    this.map.touchZoom.disable();
    this.map.doubleClickZoom.disable();
    this.map.scrollWheelZoom.disable();
    this.map.gridControl.options.follow = true;

    this.popup = new L.Popup({ autoPan: false, maxWidth:250, closeButton:false });
    this.popup_previous_name = "";

}

CityDigitsMap.loadLayerFor = function(layerId){
        //remove current layer
    if(mainLayer!=null && layerId!="VIEW_ALL_SCHOOLS"){
       MY_MAP.map.removeLayer(mainLayer);
    }
    //set fillcolor based on id and properties
    if(layerId == "PERCENT_INCOME"){
//        MY_MAP.map.removeLayer(mainLayer);
        mainLayer =L.geoJson(nyc_neighborhoods,{
            style :CityDigitsMap.getStyleColorForPercentIncome,
            onEachFeature :CityDigitsMap.onEachFeature
        }).addTo(MY_MAP.map);
        CURRENT_LAYER = "PERCENT_INCOME";
    }
    if(layerId == "MEDIAN_INCOME"){
//        MY_MAP.map.removeLayer(mainLayer);
       mainLayer= L.geoJson(nyc_neighborhoods,{
            style :CityDigitsMap.getStyleColorForMedianIncome,
           onEachFeature :CityDigitsMap.onEachFeature
        }).addTo(MY_MAP.map);
        CURRENT_LAYER = "MEDIAN_INCOME";

    }
    if(layerId == "AVG_WIN"){
//        MY_MAP.map.removeLayer(mainLayer);
       mainLayer= L.geoJson(nyc_neighborhoods,{
            style :CityDigitsMap.getStyleColorForAverageWin,
           onEachFeature :CityDigitsMap.onEachFeature
        }).addTo(MY_MAP.map);
        CURRENT_LAYER="AVG_WIN";
    }
    if(layerId == "AVG_SPEND"){
//        MY_MAP.map.removeLayer(mainLayer);
       mainLayer = L.geoJson(nyc_neighborhoods,{
            style :CityDigitsMap.getStyleColorForAverageSpend,
           onEachFeature :CityDigitsMap.onEachFeature
        }).addTo(MY_MAP.map);
        CURRENT_LAYER="AVG_SPEND";
    }
    if(layerId == "NET_GAIN_LOSS"){
//        MY_MAP.map.removeLayer(mainLayer);
       mainLayer= L.geoJson(nyc_neighborhoods,{
            style :CityDigitsMap.getStyleColorForNetWinLoss,
           onEachFeature :CityDigitsMap.onEachFeature
        }).addTo(MY_MAP.map);
        CURRENT_LAYER="NET_GAIN_LOSS";
    }
    if(layerId == "VIEW_ALL_SCHOOLS"){
        //if this is clicked while active, close it
        if(CURRENT_LAYER == "VIEW_ALL_SCHOOLS" && VIEW_ALL_SCHOOLS_IS_OPEN==true){
            $(".map-ui li.active #map-ui-subnav-content").hide();
            VIEW_ALL_SCHOOLS_IS_OPEN = false;
            //remove previous layer
            if(MARKER_LAYER!=null){
                console.log("clearing layer");
                MY_MAP.map.removeLayer(MARKER_LAYER);
            }
        }else{
            CURRENT_LAYER = "VIEW_ALL_SCHOOLS";
            VIEW_ALL_SCHOOLS_IS_OPEN = true;
        }
    }
}

CityDigitsMap.viewSwitcher = function(){
    //get active layer
    var layerId = $(".map-ui li.active").attr("id");
    console.log("LAYERID: " + layerId);
    if($.inArray(layerId,['AVG_WIN','AVG_SPEND','NET_GAIN_LOSS'])>-1){
        if(mainLayer!=null){
            MY_MAP.map.removeLayer(mainLayer);
            mainLayer = null;
        }
        if(layerId == "AVG_WIN" && !WINNINGS_LAYER){
            loadAvgWinningsMarkers();
        }else if(layerId=="AVG_SPEND" && !SPENDINGS_LAYER){
            loadAvgSpendingsMarkers();
        }else if(layerId=="NET_GAIN_LOSS" && !WINNINGS_LAYER & !SPENDINGS_LAYER){
            loadNetGainLossMarkers();
        }
    }
}

CityDigitsMap.onZoomIn = function(event){
    //check for neighborhood vs city levels
    console.log("zoom in: " + MY_MAP.map.getZoom());
    if((MY_MAP.map.getZoom() + 1 >16)){
        console.log("calling view switcher");
        //neighorhood level
        CityDigitsMap.viewSwitcher();
    }else{
        //city level
        if(WINNINGS_LAYER || SPENDINGS_LAYER){
            if(WINNINGS_LAYER){
                MY_MAP.map.removeLayer(WINNINGS_LAYER);
            }
            if(SPENDINGS_LAYER){
                MY_MAP.map.removeLayer(SPENDINGS_LAYER);
            }
            var layerId = $(".map-ui li.active").attr("id");
            if(mainLayer==null){
                CityDigitsMap.loadLayerFor(layerId);
            }
            updateMapUIBackToCityLevel();
        }
    }
    MY_MAP.map.zoomIn();
}



CityDigitsMap.onZoomOut = function(event){
        console.log("zoom out: " + MY_MAP.map.getZoom());

     if((MY_MAP.map.getZoom() + 1 >16)){
        //neighorhood level
        CityDigitsMap.viewSwitcher();
    }else{
        //city level
        if(WINNINGS_LAYER || SPENDINGS_LAYER){
            if(WINNINGS_LAYER){
                MY_MAP.map.removeLayer(WINNINGS_LAYER);
            }
            if(SPENDINGS_LAYER){
                MY_MAP.map.removeLayer(SPENDINGS_LAYER);
            }
            var layerId = $(".map-ui li.active").attr("id");
            if(mainLayer==null){
                CityDigitsMap.loadLayerFor(layerId);
            }
            updateMapUIBackToCityLevel();
        }
    }
    MY_MAP.map.zoomOut();
}



CityDigitsMap.onEachFeature = function(feature,layer){

    //set mouse events for layer
    layer.on('mouseover', function(ev) {
        CityDigitsMap.popup_previous_name = feature.properties.N_Name;
        //get lat/long
        MY_MAP.popup.setLatLng(MY_MAP.map.layerPointToLatLng(ev.layerPoint));
        MY_MAP.popup.setContent('<div class="rollover-tooltip">'+feature.properties.N_Name + '</div>');
        //display popup
        if (!MY_MAP.popup._isOpen) MY_MAP.popup.openOn(MY_MAP.map);

        });

    layer.on("mouseout",function resetHighlight(e) {
//    mainLayer.resetStyle(e.target);
    });

    layer.on('mousemove', function(ev) {
        CityDigitsMap.popup_previous_name = feature.properties.N_Name;
            //get lat/long
        MY_MAP.popup.setLatLng(MY_MAP.map.layerPointToLatLng(ev.layerPoint));
                MY_MAP.popup.setContent('<div class="rollover-tooltip">'+feature.properties.N_Name + '</div>');

        //display popup
        if (!MY_MAP.popup._isOpen) MY_MAP.popup.openOn(MY_MAP.map);
    });

    layer.on("click",function(ev){
        CityDigitsMap.popup_previous_name = feature.properties.N_Name;
            //get lat/long
        MY_MAP.popup.setLatLng(MY_MAP.map.layerPointToLatLng(ev.layerPoint));
                MY_MAP.popup.setContent('<div class="rollover-tooltip">'+feature.properties.N_Name + '</div>');

        //display popup
        if (!MY_MAP.popup._isOpen) MY_MAP.popup.openOn(MY_MAP.map);

        if(MY_SELECTED_BOROUGHS.length >= 0 && MY_SELECTED_BOROUGHS.length !=2){
            //only 1 selected, add another
            MY_SELECTED_BOROUGHS.push(ev.target);
            //highlight current layer
            layer.setStyle({
            weight: 3,
            color: '#3b3b3b',
            opacity: 1
            });

        }else{
            //clear borough
            var event = MY_SELECTED_BOROUGHS.shift();
            mainLayer.resetStyle(event);
            //highlight current layer
            layer.setStyle({
            weight: 3,
            color: '#3b3b3b',
            opacity: 1
            });
            MY_SELECTED_BOROUGHS.push(ev.target);
        }
        //show neighborhood popup
        showMapPopUp(ev,feature);
    });

}



CityDigitsMap.prototype.loadLayers =  function (){
    var self = this;
    console.log("LOADING LAYERS");
    //show map ui nav
    $("#map-nav").load("/map/nav/");

    //add neighborhoods
    this.neighborhoodLayer = L.geoJson(nyc_neighborhoods,{
        style :CityDigitsMap.getStyleColorForPercentIncome,
        onEachFeature : CityDigitsMap.onEachFeature
    }).addTo(this.map);
//    this.neighborhoodLayer.on('mousemove', function(e) {
//        self.mapMouseMove(e);
//    });
//    this.neighborhoodLayer.on('mouseover', function(e) {
//        self.mapMouseMove(e);
//    });
//    this.neighborhoodLayer.on('mouseout', function(e) {
//        self.mapMouseOut(e);
//    });
//    this.neighborhoodLayer.on('click', function(e) {
//        self.mapMouseMove(e);
//        //load popup
//        showMapPopUp(e);
//    });
}

CityDigitsMap.prototype.resizeMap = function(){
    //set params
    this.height = $(window).height()-$(".navbar").height();
    this.width = $(window).width();
    $("#map").height(this.height);
    $("#map").width(this.width);
}

CityDigitsMap.prototype.mapMouseMove = function (ev){
    //get layer
    var layer = ev.layer;

    //verify feature
    if(layer.feature != undefined){
        this.popup_previous_name = layer.feature.properties.N_Name;
            //get lat/long
        this.popup.setLatLng(MY_MAP.map.layerPointToLatLng(ev.layerPoint));
        this.popup.setContent(layer.feature.properties.N_Name);
        //display popup
        if (!this.popup._map) this.popup.openOn(this.map);
//        window.clearTimeout(this.closeTooltip);
    }else{
        this.popup.setLatLng(MY_MAP.map.layerPointToLatLng(ev.layerPoint));
        this.popup.setContent(this.popup_previous_name);
        //display popup
        if (!this.popup._map) this.popup.openOn(this.map);
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
        weight: 1,
        opacity: .1,
        color: 'white',
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
         weight: 1,
         opacity: 0.1,
         color: 'white',
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
         weight: 1,
         opacity: 0.1,
         color: 'white',
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
         weight: 1,
         opacity: 0.1,
         color: 'white',
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
         weight: 1,
         opacity: 0.1,
         color: 'white',
         fillOpacity: 0.75,
         fillColor: fillColor
    }

}
