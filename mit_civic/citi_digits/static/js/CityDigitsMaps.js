function CityDigitsMap() {
    //init values
    this.closeTooltip = null;
    this.neighborhoodLayer = null;

    //load map
    var basemap = "sw2279.NYCLotto";

    this.map = L.mapbox.map('map', basemap);
    //set params
    this.height = $(window).height()-$(".navbar").height();
    this.width = $(window).width();

     //disable unwanted events
    this.map.touchZoom.disable();
    this.map.doubleClickZoom.disable();
    this.map.scrollWheelZoom.disable();
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
        style : {
            weight: 0,
            opacity: 0.1
        }
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
    //get lat/long
    this.popup.setLatLng(ev.latlng);
    this.popup.setContent(layer.feature.properties.N_Name);
    //display popup
    if (!this.popup._map) this.popup.openOn(this.map);
    window.clearTimeout(this.closeTooltip);
}

CityDigitsMap.prototype.mapMouseOut = function(e) {
    var self = this;
    this.neighborhoodLayer.resetStyle(e.target);
    this.closeTooltip = window.setTimeout(function() {
        self.map.closePopup();
        }, 100);
}