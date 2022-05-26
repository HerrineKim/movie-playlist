<template>
  <div>
    <nav-bar></nav-bar>
    <br>
    <br>

    <account-error-list v-if="isAuthError"></account-error-list>
    
    <div class="container">
      <div class="container col-5 my-3">
        <form @submit.prevent="login(credentials)">
          <div class="form-outline">
            <label class="form-label" for="username"></label>
            <input placeholder="username" class="form-control" v-model="credentials.username" type="text" id="username" required>
          </div>
          <div class="form-outline mb-4">
            <label class="form-label" for="password"></label>
            <input placeholder="password" class="form-control" v-model="credentials.password" type="password" id="password" required>
          </div>

          <button class="btn btn-outline-secondary waves-effect mb-4">로그인</button>
        </form>
      </div>
    </div>
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