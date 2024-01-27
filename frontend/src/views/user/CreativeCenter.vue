<script setup lang="ts">

import {ref, watch} from "vue";
import {baseURL} from "@/services/requests/config";
import Input from "@/views/user/cpn/Input.vue";
import Output from "@/views/user/cpn/Output.vue";

let uploadInfo = ref({
  method: "POST",
  action: baseURL + "/upload",
  headers: {
    Authorization: "Bearer " + sessionStorage.getItem("token")
  }
})
let inputData = ref({
  model: [
    {
      id: 1,
      name: "模型1"
    },
    {
      id: 2,
      name: "模型2"
    }
  ],
  uploadInfo: {
    name: "images",
    method: "POST",
    action: baseURL + "/image",
    headers: {
      Authorization: "Bearer " + sessionStorage.getItem("token")
    }
  },
  imageUrl: ""
})
</script>

<template>
  <div class="creation">
    <Input class="select-image" v-model="inputData"></Input>
    <Output class="out-image" v-model="inputData.imageUrl"></Output>
  </div>
</template>

<style>
.creation{
  display: flex;
  flex-direction: row;
  justify-content: space-between;

}
.select-image {
  width: 45%;
  height: Calc(100vh - 100px);
  margin: 0 auto 0 0;
}
.out-image{
  width: 45%;
  //height: Calc(100vh - 300px);
  margin: 0 0 0 auto;
}
</style>