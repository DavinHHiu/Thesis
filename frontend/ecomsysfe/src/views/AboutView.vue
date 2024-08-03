<template>
  <div class="body">
    <div class="wp">
      <custom-label :required="true">Email</custom-label>
      <custom-input placeholder="hddfdf" />
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import CustomInput from '../components/common/atomic/CustomInput.vue';
import CustomLabel from '../components/common/atomic/CustomLabel.vue';

export default defineComponent({
  name: 'AboutView',
  components: {
    CustomInput,
    CustomLabel,
  },
});
</script>
<style scoped>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}

.body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.wp {
  height: 4rem;
  width: 10rem;
}
</style>
