<template>
  <div class="ost">
    <img src="" alt="">
    <nav-bar-ost></nav-bar-ost>
    <div></div>
    <img src="@/assets/images/Header2.png" alt="">
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
  background-color:black;
}

</style>