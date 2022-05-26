<template>
  <div>
    <nav-bar></nav-bar>
    <h1 style="font-family: 'GmarketSansMedium';">
      Logout 되었습니다.
    </h1>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'LogoutView',
  components: {
    NavBar
  },
  methods: {
    ...mapActions(['logout'])
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  created() {
    if (this.isLoggedIn) {
      this.logout()
    } else {
      alert('잘못된 접근입니다.')
      this.$router.back()
    }
  }
}
</script>

<style>

</style>