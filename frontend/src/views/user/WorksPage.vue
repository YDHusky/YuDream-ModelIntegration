<script setup lang="ts">
import {get_works_md} from "@/services/modules/works";
import {onMounted, ref} from "vue";
import WorkCard from "@/views/user/cpn/WorkCard.vue";
let works_list = ref([])
async function getWorks(){
  let works = await get_works_md()
  works_list.value = works.data
  console.log(works_list.value)
}

onMounted(()=>{
  getWorks()
})
</script>

<template>
  <WorkCard v-model="works_list">

  </WorkCard>
</template>

<style scoped>

</style>