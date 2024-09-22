<template>
  <page-title :title="$t('userPage.list.title')" />
  <page-body>
    <header-action :current-route="$t('userPage.add.name')" />
    <tab-layout />
    <table class="w-full mt-[2rem] overflow-hidden">
      <thead>
        <tr>
          <th>No.</th>
          <th>Avatar</th>
          <th>Email</th>
          <th>First name</th>
          <th>Last name</th>
          <th>Date of birth</th>
          <th>Tel</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(user, index) in users" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td>{{ index + 1 }}</td>
            <td>
              <div class="flex justify-center">
                <img
                  :src="user.avatar as string"
                  :alt="user.email"
                  class="w-[4rem] h-[4rem] rounded-full object-cover"
                />
              </div>
            </td>
            <td v-text="user.email || '_'" />
            <td v-text="user.first_name || '_'" />
            <td v-text="user.last_name || '_'" />
            <td v-text="user.birth_of_date || '_'" />
            <td v-text="user.tel || '_'" />
            <td class="action-wrap">
              <ellipsis-dropdown
                @action="handleActions"
                :current-index="index"
                :dropdown-list="[
                  { title: 'Update', action: '' },
                  { title: 'Delete', action: '#deleteModal' },
                ]"
              />
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </page-body>
  <modal id="deleteModal" title="Delete attribute" @confirm="submitAction">
    <span v-text="$t('productPage.modalDelete.title')" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useUserStore } from "@/stores/user";
import { User } from "@/types/worker";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "UserView",
  components: {
    CustomButton,
    EllipsisDropdown,
    Modal,
    HeaderAction,
    PageTitle,
    PageBody,
  },
  data() {
    return {
      currentAction: "" as string,
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useUserStore, ["listUsers", "destroyUser"]),
    handleActions(obj: any) {
      const user = this.users[obj.currentIndex];
      if (obj.action === "Update") {
        this.$router.push({
          name: "user.update",
          params: { id: user.id },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    async submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const user = this.users[this.currentIndex] as User;
        if (user.id) {
          this.destroyUser(user.id);
        }
      }
    },
  },
  computed: {
    ...mapState(useUserStore, ["users"]),
  },
  async mounted() {
    await this.listUsers();
  },
});
</script>

<style lang="scss" scoped></style>
