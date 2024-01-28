<script setup lang="ts">

import ModelCard from "@/views/admin/cpn/ModelCard.vue";
import {getModelList_md} from "@/services/modules/model";
import {onMounted, ref} from "vue";

let models = ref()
async function get_model_info(){
  let model = await getModelList_md()
  models.value = model['data']
}
onMounted(()=>{
  get_model_info()
})
</script>

<template>
  <ModelCard v-model="models"></ModelCard>
</template>

<style scoped>

</style>