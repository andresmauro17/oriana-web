<template>
  <div>
    <h1>mainlayout</h1>
    <slot name="content"></slot>
  </div>
</template>

<script>
import { onMounted} from "vue";
export default {
  setup () {
    onMounted(()=>{
      console.log("mainlayout mounted")
    })

    return {}
  }
}
</script>

