<template>
  <div class="home">
    <nav-bar></nav-bar>
    <div>
      <widgets-organism></widgets-organism>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar.vue'
import WidgetsOrganism from '@/components/organisms/Home/WidgetsOrganism.vue'
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    WidgetsOrganism, NavBar
  },
}
</script>
