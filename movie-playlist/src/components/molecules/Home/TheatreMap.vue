<template>
  <div>
    <div>
      <!-- <button @click='geofind'>위치찾기</button>
      <p> {{textContent}} </p> -->
      <div id="map" style="width:500px;height:400px;"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TheatreMap",
  // data () {
  //   return {
  //       latitude: '',
  //       longitude: '',
  //       textContent: ''
  //   }
  // },
  // methods: {
  //   geofind() {
  //     if(!("geolocation" in navigator)) {
  //     this.textContent = 'Geolocation is not available.';
  //     return;
  //     }
  //     this.textContent = 'Locating...'
      
  //     // get position
  //     navigator.geolocation.getCurrentPosition(pos => {
  //     this.latitude = pos.coords.latitude;
  //     this.longitude = pos.coords.longitude;
  //     this.textContent = 'Your location data is ' + this.latitude + ', ' + this.longitude
  //     }, err => {
  //     this.textContent = err.message;
  //     })
  //   }
  // }
  
}

</script>

<style>

</style>