function initMap(): void {
    console.log(11)
    console.log(document.getElementById("map"))
    const map = new google.maps.Map(
        document.getElementById("map") as HTMLElement,
        {
            zoom: 3,
            center: {lat: 0, lng: -180},
            mapTypeId: "terrain",
        }
    );

    const flightPlanCoordinates = [
        {lat: 37.772, lng: -122.214},
        {lat: 21.291, lng: -157.821},
        {lat: -18.142, lng: 178.431},
        {lat: -27.467, lng: 153.027},
    ];
    const flightPath = new google.maps.Polyline({
        path: flightPlanCoordinates,
        geodesic: true,
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 2,
    });

    flightPath.setMap(map);
    console.log(11)

}

declare global {
    interface Window {
        initMap: () => void;
    }
}
window.initMap = initMap;
export {};

