<template>
  <div class="actors">
    <h2>영화배우 데이터 리스트로 보여주고, 클릭하면 detail 나오는 기능</h2>
    <div v-for="actor in actors" :key="actor.id">
      <router-link :to="{ name: 'actor', params: { actorPk: actor.id } }">{{ actor.name}}</router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ActorsView',
  components: {
  },
  computed: {
    ...mapGetters(['actors'])
  },
  methods: {
    ...mapActions(['fetchActors'])
  },
  created() {
    this.fetchActors()
  },
}
</script>

<style>

</style>