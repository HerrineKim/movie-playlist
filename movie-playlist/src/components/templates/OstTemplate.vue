<template>
  <div>
    <player-organism></player-organism>
    <br>
    <ost-list-organism></ost-list-organism>
  </div>
</template>

<script>
import OstListOrganism from '../organisms/Ost/OstListOrganism.vue'
import PlayerOrganism from '../organisms/Ost/PlayerOrganism.vue'
export default {
  name: "OstTemplate",
  components: {PlayerOrganism, OstListOrganism}
}
</script>

<style>

</style>