<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar.vue'

export default {
  name: 'App',
  components: { NavBar },
  methods: {
    fetchCurrentUser () {
      this.$store.dispatch('fetchCurrentUser')
    },
    fetchBoxoffice () {
      this.$store.dispatch('fetchBoxoffice')
    },
  },
  created () {
    this.fetchBoxoffice()
    this.fetchCurrentUser()
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
