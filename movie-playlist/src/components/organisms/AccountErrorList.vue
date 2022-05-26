<template>
  <div class="account-error-list">
    <p style="font-family: 'GmarketSansMedium';" v-for="(errors, field) in authError" :key="field">
        <span v-for="(error, idx) in errors" :key="idx">
          {{ error }} ㅠㅠ
        </span>
    </p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'AccountErrorList',
  computed: {
    ...mapGetters(['authError'])
  }
}
</script>

<style>
</style>