<template>
  <div class="home">
    <div>
      <widgets-organism></widgets-organism>
    </div>
  </div>
</template>

<script>
import WidgetsOrganism from '@/components/organisms/Home/WidgetsOrganism.vue'
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    WidgetsOrganism,
  },
}
</script>
