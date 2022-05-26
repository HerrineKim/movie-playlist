<template>
  <div>
    <nav-bar></nav-bar>
    <account-error-list v-if="isAuthError"></account-error-list>
    <div class="container" style="text-align: left; padding:100px;">
      <form @submit.prevent="signup(credentials)">
        <div>
          <label class="form-label" for="username"></label>
          <input placeholder="아이디를 입력하세요" class="form-control" type="text" id="username" v-model="credentials.username" required>
        </div>
        <div>
          <label class="form-label" for="password1"></label>
          <input placeholder="비밀번호를 입력하세요" class="form-control" type="password" id="password1" v-model="credentials.password1" required>
        </div>
        <div>
          <label class="form-label" for="password2"></label>
          <input placeholder="비밀번호를 다시 한 번 입력하세요" class="form-control" type="password" id="password2" v-model="credentials.password2" required>
        </div>
        <br>
        <div>
          <button class="btn btn-outline-secondary waves-effect mb-4">Signup</button>
        </div>
      </form>
    </div>

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