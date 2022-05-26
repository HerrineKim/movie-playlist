<template>
  <div class="ost">
    <nav-bar-ost></nav-bar-ost>
    <ost-template></ost-template>
  </div>
</template>

<script>
  import NavBarOst from "@/components/templates/NavBarOst.vue"
  import OstTemplate from "@/components/templates/OstTemplate.vue"


  export default {
    name: 'OstView',
    components: {
      OstTemplate, NavBarOst
    },
  }
</script>

<style scoped>
.ost  {
  background-image:url(@/assets/images/Header2.png);
  background-repeat: no-repeat;
  background-position: center top;
  background-color: black;
}

</style>