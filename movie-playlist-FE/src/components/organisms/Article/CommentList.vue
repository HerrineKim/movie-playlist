<template>
  <div class="comment-list">
    <comment-list-item 
      v-for="comment in comments" 
      :comment="comment" 
      :key="comment.pk">
    </comment-list-item>        
    <br>
    <br>
    <comment-list-form></comment-list-form>
  </div>
</template>

<script>
import CommentListItem from '@/components/molecules/Article/CommentListItem.vue'
import CommentListForm from '@/components/molecules/Article/CommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentListForm, CommentListItem },
  props: { comments: Array },
}
</script>

<style>

</style>