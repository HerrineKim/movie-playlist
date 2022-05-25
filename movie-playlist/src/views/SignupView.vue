<template>
  <div>
    <nav-bar></nav-bar>
    <h1>Signup</h1>

    <account-error-list v-if="isAuthError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username">Username: </label>
        <input type="text" id="username" v-model="credentials.username" required>
      </div>
      <div>
        <label for="password1">Password: </label>
        <input type="password" id="password1" v-model="credentials.password1" required>
      </div>
      <div>
        <label for="password2">Password Confirmation:</label>
        <input type="password" id="password2" v-model="credentials.password2" required>
      </div>
      <div>
        <button>Signup</button>
      </div>
    </form>
  </div>
</template>

<script>
import NavBar from "@/components/templates/NavBar.vue"
import AccountErrorList from '@/components/organisms/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  components: { AccountErrorList, NavBar },
  name: 'SignupView',
  data() {
    return {
      credentials: {
        username: '',
        password1: '',
        password2: '',
      },
    }
  },
  computed: {
    ...mapGetters(['isAuthError'])
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>

<style>

</style>