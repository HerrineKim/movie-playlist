<template>
  <div class="home">
    <Navbar></Navbar>
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Navbar from '@/components/templates/Navbar.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
    Navbar,
  }
}
</script>
