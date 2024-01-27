<script setup lang="ts">
import {onMounted, ref, watch} from "vue";
import type {UploadInstance} from "element-plus";
import {UploadFilled} from "@element-plus/icons-vue";
import {getModelList_md} from "@/services/modules/model";

const data = defineModel()
let value = ref('')
let uploadInfo = ref(data.value.uploadInfo)
let uploadRef = ref<UploadInstance>()
const submitUpload = () => {
  uploadRef.value!.submit()
}
const returnData = (res) => {
  data.value.imageUrl = res.data[0]
}
let model_list = ref([])

onMounted(()=>{
  getModelList_async()
})
async function getModelList_async() {
  let modelList = await getModelList_md()
  model_list.value = modelList['data']
  console.log(model_list.value)
}
let post_data = ref({
  "model_name": value.value,
})
watch(value, (newVal, oldVal) => {
  post_data.value = {
    "model_name": newVal,
  }
})

</script>

<template>
  <el-card header="输入调整">
    <el-select v-model="value" placeholder="选择一个模型">
      <el-option v-for="item in model_list" :key="item['name']" :label="item['displayName']" :value="item['name']">

      </el-option>
    </el-select>
    <el-upload
        drag
        class="upload"
        ref="uploadRef"
        :data="post_data"
        :name="uploadInfo.name"
        :method="uploadInfo.method"
        :auto-upload="false"
        :headers="uploadInfo.headers"
        :action="uploadInfo.action"
        :on-success="returnData"
    >
      <el-icon class="el-icon--upload">
        <upload-filled/>
      </el-icon>
      <div class="el-upload__text">
        拖动一张图片到这<br/>
        <em>点击选择一张图片</em>
      </div>
      <template #tip>
        <div class="el-upload__tip">
          只能选择一张图片
        </div>
      </template>
    </el-upload>
    <el-button type="primary" class="conversion-button" @click="submitUpload">转换图片</el-button>
  </el-card>
</template>

<style scoped>
.upload {
  margin-top: 20px;
}

.conversion-button {
  margin-top: 20px;
  width: 100%;
}
</style>