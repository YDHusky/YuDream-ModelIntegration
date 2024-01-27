<script setup lang="ts">

import {onMounted, ref} from "vue";
import {getOption_md} from "@/services/modules/option";

let announcement = ref()
async function announcement_async(){
  let data = await getOption_md("announcement")
  announcement.value = data['data']['value']
}
onMounted(() => {
  announcement_async()
})
</script>

<template>
  <el-card header="公告">
    <div class="announcement">
      {{announcement}}
    </div>
  </el-card>
</template >

<style scoped>

</style>