<script setup lang="ts">
import {ref, watch} from "vue";
import {ElNotification} from "element-plus";
import {delete_works_md, update_works_md} from "@/services/modules/works";

let works = defineModel()
let drawer = ref(false)
let work = ref()
const handleSelect = (id: any) => {
  drawer.value = true
  work.value = get_work(id)
}
let work_name = ref('')
const get_work = (id: any) => {
  for (let i = 0; i < works.value.length; i++) {
    if (works.value[i]['id'] === id) {
      return works.value[i]
    }
  }
}
const get_original_url = (url: any) => {
  return url.replace('out', 'in')
}
watch(work, (newVal) => {
  work_name.value = newVal['work_name']
})
const submit_work = () => {
  if (work_name.value === "") {
    ElNotification({
      title: "作品名字不能为空",
      type: "error"
    })
  }
  if (work_name.value === work.value['work_name']) {
    ElNotification({
      title: "作品名字没有改变",
      type: "warning"
    })
  }
  else {
    submit_work_async()
  }
}
async function submit_work_async() {
  let res = await update_works_md(work.value['id'], work_name.value)
  if (res.code === 200) {
    ElNotification({
      title: "保存成功",
      type: "success"
    })
  }
  else {
    ElNotification({
      title: "保存失败",
      type: "error"
    })
  }
}
async function del_work_async() {
  let res = await delete_works_md(work.value['id'])
  if (res.code === 200) {
    ElNotification({
      title: "删除成功",
      type: "success"
    })
  }
  else {
    ElNotification({
      title: "删除失败",
      type: "error"
    })
  }
}
const del_work = () => {
  del_work_async()
}
</script>

<template>
  <div class="work-card">
    <el-card v-for="work in works">
      <el-image style="height: 200px; margin-bottom: 5px" :src="work['url']"/>
      <el-descriptions
          border
          :column="1"
      >
        <el-descriptions-item label="作品名字">{{ work['work_name'] }}</el-descriptions-item>
        <el-descriptions-item label="作者">{{ work['username'] }}</el-descriptions-item>
        <el-descriptions-item label="作品创建时间">{{ work['create_time'] }}</el-descriptions-item>
      </el-descriptions>
      <el-button @click="handleSelect(work['id'])" class="edit-bt">编辑作品</el-button>
    </el-card>
  </div>
  <el-drawer
      v-model="drawer"
      title="编辑作品"
      direction="rtl"
  >
    <el-scrollbar>
      <el-collapse>
        <el-collapse-item title="原图">
          <el-image style="height: 200px; margin-bottom: 5px" :src="get_original_url(work['url'])"/>
        </el-collapse-item>
        <el-collapse-item title="作品图">
          <el-image style="height: 200px; margin-bottom: 5px" :src="work['url']"/>
        </el-collapse-item>
        <el-collapse-item title="修改作品名字">
          <el-input v-model="work_name"></el-input>
        </el-collapse-item>
      </el-collapse>
    </el-scrollbar>
    <template #footer>
      <el-button @click="drawer=false">取 消</el-button>
      <el-button @click="del_work()" type="danger">删 除</el-button>
      <el-button @click="submit_work" type="success">确 定</el-button>
    </template>
  </el-drawer>

</template>

<style>
.work-card {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 0 auto;
  width: 100%;
  height: 100%;

  .el-card {
    margin: 10px 0;
  }
}

.edit-bt {
  margin-top: 10px;
  width: 100%;
}
</style>