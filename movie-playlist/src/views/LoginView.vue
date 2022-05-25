<template>
  <div>
    <nav-bar></nav-bar>
    <h1>Login</h1>

    <account-error-list v-if="isAuthError"></account-error-list>

    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">username: </label>
        <input v-model="credentials.username" type="text" id="username" required>
      </div>

      <div>
        <label for="password">password: </label>
        <input v-model="credentials.password" type="password" id="password" required>
      </div>

      <button>Login</button>
    </form>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar.vue'
import AccountErrorList from '@/components/organisms/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  components: { AccountErrorList, NavBar },
  name: 'LoginView',
  data () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapGetters(['isAuthError'])
  },
  methods: {
    ...mapActions(['login'])
  },
}
</script>

<style>
.error-messages {
  color: red;
}
</style>