<script setup lang="ts">
import { ref} from "vue";
import Statistics from "@/views/user/cpn/Statistics.vue";
import Announcement from "@/views/user/cpn/Announcement.vue";
</script>

<template>
  <div class="user-page">
    <div class="statistic">
      <Statistics></Statistics>
    </div>
    <div class="announcement">
      <Announcement></Announcement>
    </div>
  </div>
</template>

<style>
.user-page{
  width: 100%;
  height: 100%;
  display: flex;
  .statistic{
    width: 50%;
    height: 100%;
    margin: 0 10px 0 0;
  }
  .announcement{
    width: 50%;
    height: 100%;
    margin: 0 0 0 10px;
  }
}
</style>