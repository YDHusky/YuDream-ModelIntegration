<script setup lang="ts">
import {ref} from "vue";
import {editModel_md} from "@/services/modules/model";
import {ElNotification} from "element-plus";

let models = defineModel()
let modelDrawer = ref(false)
let model = ref()
const handleSelect = (item) => {
  modelDrawer.value = true
  model.value = item
}

async function update_model_info() {
  let data = {
    'displayName': model.value['displayName'],
    'name': model.value['name'],
    'description': model.value['description'],
    'version': model.value['version'],
    'author': model.value['author'],
  }
  if (data['displayName'] === "") {
    ElNotification({
      title: "模型本地化名不能为空",
      type: "error"
    })
    return
  }
  if (data['name'] === "") {
    ElNotification({
      title: "模型名字不能为空",
      type: "error"
    })
    return
  }
  if (data['description'] === "") {
    ElNotification({
      title: "模型描述不能为空",
      type: "error"
    })
    return
  }
  if (data['version'] === "") {
    ElNotification({
      title: "模型版本不能为空",
      type: "error"
    })
    return
  }
  if (data['author'] === "") {
    ElNotification({
      title: "模型作者不能为空",
      type: "error"
    })
    return
  }

    let res = await editModel_md(data)
    if (res.code === 200) {
      ElNotification({
        title: "保存成功",
        type: "success"
      })
    } else {
      ElNotification({
        title: "保存失败",
        type: "error"
      })
    }

}
</script>

<template>
  <div class="model-card">
    <el-card v-for="item in models">
      <el-descriptions
          :column="1"
          border
      >
        <el-descriptions-item label="模型本地化名">{{ item['displayName'] }}</el-descriptions-item>
        <el-descriptions-item label="模型名字">{{ item['name'] }}</el-descriptions-item>
        <el-descriptions-item label="模型描述">{{ item['description'] }}</el-descriptions-item>
        <el-descriptions-item label="模型版本">{{ item['version'] }}</el-descriptions-item>
        <el-descriptions-item label="模型作者">{{ item['author'] }}</el-descriptions-item>
        <el-descriptions-item label="模型文件夹名">{{ item['modelDir'] }}</el-descriptions-item>
      </el-descriptions>
      <el-button @click="handleSelect(item)">
        编辑模型信息
      </el-button>
    </el-card>
    <el-drawer
        v-model="modelDrawer"
        title="编辑模型信息"
        direction="rtl">
      <el-collapse>
        <el-collapse-item title="模型本地化名">
          <el-input v-model="model['displayName']"></el-input>
        </el-collapse-item>
        <el-collapse-item title="模型名字">
          <el-input disabled v-model="model['name']"></el-input>
        </el-collapse-item>
        <el-collapse-item title="模型描述">
          <el-input v-model="model['description']"></el-input>
        </el-collapse-item>
        <el-collapse-item title="模型版本">
          <el-input v-model="model['version']"></el-input>
        </el-collapse-item>
        <el-collapse-item title="模型作者">
          <el-input v-model="model['author']"></el-input>
        </el-collapse-item>
      </el-collapse>
      <template #footer>
        <el-button @click="modelDrawer=false">取 消</el-button>
        <el-button type="primary" @click="update_model_info">确 定</el-button>
      </template>
    </el-drawer>
  </div>
</template>

<style>
.model-card {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 0 auto;
  width: 100%;
  height: 100%;

  .el-card {
    .el-button {
      margin-top: 15px;
      width: 100%;
    }
  }
}
</style>