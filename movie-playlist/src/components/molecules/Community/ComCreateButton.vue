<template>
  <div v-if="isLoggedIn">
    <router-link :to="{ name: 'articleNew' }">
      <button>New</button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "ComCreateButton",
}
</script>

<style>

</style>