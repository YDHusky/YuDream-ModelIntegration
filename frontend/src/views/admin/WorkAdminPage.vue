<script setup lang="ts">

import WorkCard from "@/views/user/cpn/WorkCard.vue";
import {onMounted, ref} from "vue";
import {get_all_works_md} from "@/services/modules/works";

let works = ref()
async function get_all_works_async(){
  const res = await get_all_works_md()
  works.value = await res.data
}
onMounted(()=>{
  get_all_works_async()
})
</script>

<template>
  <WorkCard v-model="works"></WorkCard>
</template>

<style scoped>

</style>