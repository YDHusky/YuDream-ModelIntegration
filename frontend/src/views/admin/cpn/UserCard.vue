<script setup lang="ts">
import {ref} from "vue";
import {delete_user_by_admin, update_user_by_admin, update_user_password_by_admin} from "@/services/modules/user";
import {ElNotification} from "element-plus";

let user_list = defineModel()
let userDrawer = ref(false)
let user = ref()
let password = ref('')
const handleSelect = (item) => {
  userDrawer.value = true
  user.value = item
}
async function update_user_info() {
  let res = await update_user_by_admin(user.value)
  if (res['code'] === 200) {
    userDrawer.value = false
    ElNotification({
      title: '成功',
      message: '用户信息更新成功',
      type: 'success'
    })
  }
  else {
    ElNotification({
      title: '失败',
      message: '用户信息更新失败',
      type: 'error'
    })
  }
}
async function update_user_password(){
  if (password.value===""){
    ElNotification({
      title: '失败',
      message: '密码不能为空',
      type: 'error'
    })
  }
  else {
    let res = await update_user_password_by_admin({'username':user.value['username'],'password':password.value})
    if (res['code'] === 200) {
      userDrawer.value = false
      ElNotification({
        title: '成功',
        message: '用户密码更新成功',
        type: 'success'
      })
    }
    else {
      ElNotification({
        title: '失败',
        message: '用户密码更新失败',
        type: 'error'
      })
    }
  }
}
async function delete_user(){
  if (user.value['role']===3){
    ElNotification({
      title: '失败',
      message: '不能删除管理员',
      type: 'error'
    })
  }
  else {
    let data = await delete_user_by_admin(user.value['username'])
    ElNotification({
      title: '成功',
      message: '用户删除成功',
      type: 'success'
    })
  }

}
</script>

<template>
  <div class="user-card">
    <el-card v-for="item in user_list">
      <el-descriptions
          border
          :column="1"
      >
        <el-descriptions-item label="用户ID">{{ item['id'] }}</el-descriptions-item>
        <el-descriptions-item label="用户名">{{ item['username'] }}</el-descriptions-item>
        <el-descriptions-item label="昵称">{{ item['nickname'] }}</el-descriptions-item>
        <el-descriptions-item label="邮箱">{{ item['email'] }}</el-descriptions-item>
        <el-descriptions-item label="手机">{{ item['phone'] }}</el-descriptions-item>
        <el-descriptions-item label="用户角色">{{ item['role'] }}</el-descriptions-item>
        <el-descriptions-item label="用户创建时间">{{ item['create_time'] }}</el-descriptions-item>
      </el-descriptions>
      <el-button @click="handleSelect(item)">编辑用户</el-button>
    </el-card>
  </div>
  <el-drawer
      v-model="userDrawer"
      title="编辑用户">
    <el-scrollbar>
      <el-collapse>
        <el-collapse-item title="用户ID">
          <el-input disabled v-model="user['id']"></el-input>
        </el-collapse-item>
        <el-collapse-item title="用户名">
          <el-input disabled v-model="user['username']"></el-input>
        </el-collapse-item>
        <el-collapse-item title="昵称">
          <el-input v-model="user['nickname']"></el-input>
        </el-collapse-item>
        <el-collapse-item title="邮箱">
          <el-input v-model="user['email']"></el-input>
        </el-collapse-item>
        <el-collapse-item title="手机">
          <el-input v-model="user['phone']"></el-input>
        </el-collapse-item>
        <el-collapse-item title="角色">
          <el-select v-model="user['role']">
            <el-option label="管理员" value="3"></el-option>
            <el-option label="普通用户" value="1"></el-option>
          </el-select>
        </el-collapse-item>
        <el-collapse-item title="密码">
          <el-input placeholder="请输入要修改的密码" v-model="password">
            <template #append>
              <el-button @click="update_user_password">修改密码</el-button>
            </template>
          </el-input>
        </el-collapse-item>
      </el-collapse>
    </el-scrollbar>
    <template #footer>
      <el-button @click="userDrawer=false">取 消</el-button>
      <el-button @click="delete_user" type="danger">删除</el-button>
      <el-button type="success" @click="update_user_info">确 定</el-button>
    </template>
  </el-drawer>

</template>

<style scoped>
.user-card {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 0 auto;
  width: 100%;
  height: 100%;

  .el-card {
    margin-bottom: 10px;
    .el-button {
      margin-top: 15px;
      width: 100%;
    }
  }
}

</style>