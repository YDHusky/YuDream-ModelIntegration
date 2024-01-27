<script setup lang="ts">
import {ref, watch} from "vue";
import {save_works_md} from "@/services/modules/works";
import {ElMessage} from "element-plus";

let imageUrl = defineModel()
let isShow = ref(true)
let workName = ref("")
watch(imageUrl, (newVal) => {
  if (newVal) {
    isShow.value = false
  }
})
async function save_work_async(){
  if (workName.value === "") {
    ElMessage.error("作品名字不能为空")
    return
  }
  else {
    let res = await save_works_md(workName.value, imageUrl.value)
    if (res.code === 200) {
      ElMessage.success("保存成功")
    }
    else {
      ElMessage.error("保存失败")
    }
  }
}
const save_work = () => {
  save_work_async()
}
</script>

<template>
  <el-card class="output" header="输出预览">
    <el-scrollbar height="30%">
      <div v-loading="isShow">
        <el-image class="image" fit="contain" :src="imageUrl"></el-image>
        <el-input v-model="workName" placeholder="作品名字"></el-input>
        <el-button class="out-button" @click="save_work" type="primary">保存到我的作品</el-button>
      </div>
    </el-scrollbar>
  </el-card>

</template>

<style scoped>
.out-button {
  width: 100%;
  margin: 10px auto 5px auto;
}

.image {
  max-width: 100%;
  max-height: 400px;
}
</style>