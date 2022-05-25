<template>
  <div id="app" style="overflow:hidden;">
    <nav-bar></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {},
  data () {
    return {
      userPk: ''
    }
  },
  computed: {
    ...mapGetters([ 'currentUser' ])
  },
  methods: {
    fetchCurrentUser () {
      this.$store.dispatch('fetchCurrentUser')
      this.userPk = this.currentUser.id
    },
    fetchBoxoffice () {
      this.$store.dispatch('fetchBoxoffice')
    },
    fetchActors () {
      this.$store.dispatch('fetchActors')
    },
    // recommendation () {
    //   this.$store.dispatch('recommendation')
    // },
  },
  created () {
    this.fetchBoxoffice()
    this.fetchActors()
    this.fetchCurrentUser()
    // this.recommendation({ userPk: this.userPk })

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
