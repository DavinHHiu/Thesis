<template>
  <page-title :title="$t('userPage.list.title')" />
  <page-body>
    <header-action :current-route="$t('userPage.add.name')" />
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
          <tr :class="{ odd: !(index % 2) }">
            <td v-text="index + 1" />
            <td>
              <div class="flex justify-center">
                <img
                  :src="fmt(user.avatar)"
                  :alt="user.email"
                  class="w-[4rem] h-[4rem] rounded-full object-cover"
                />
              </div>
            </td>
            <td v-text="fmt(user.email)" />
            <td v-text="fmt(user.first_name)" />
            <td v-text="fmt(user.last_name)" />
            <td v-text="fmt(user.birth_of_date)" />
            <td v-text="fmt(user.tel)" />
            <td class="action-wrap">
              <ellipsis-dropdown
                @action="handleActions"
                :current-index="index"
                :dropdown-list="[
                  { title: 'Update', action: 'update' },
                  { title: 'Delete', action: 'openModal' },
                ]"
              />
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </page-body>
  <paging-number
    :paging="paging"
    :cur-page="currentPage"
    @change-page="changePage"
  />
  <modal
    ref="deleteModal"
    id="deleteModal"
    title="Delete attribute"
    @confirm="handleDelete"
  >
    <span v-text="$t('productPage.modalDelete.title')" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PagingNumber from "@/components/common/molecules/PagingNumber.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useUserStore } from "@/stores/user";
import { User } from "@/types/worker";
import { fmt } from "@/utils/string";
import { getPaginationRange } from "@/utils/utils";
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
    PagingNumber,
  },
  data() {
    return {
      currentIndex: 0 as number,
      resultsCount: 0,
      limit: 50,
      offset: 0,
      currentPage: 1,
    };
  },
  methods: {
    ...mapActions(useUserStore, ["listUsers", "destroyUser"]),
    handleActions(obj: any) {
      const user = this.users[obj.currentIndex];
      if (obj.action === "update") {
        this.$router.push({
          name: "user.update",
          params: { id: user.id },
        });
      } else if (obj.action === "openModal") {
        const modal = this.$refs.deleteModal as InstanceType<typeof Modal>;
        modal.open();
      }
      this.currentIndex = obj.currentIndex;
    },
    async handleDelete() {
      const user = this.users[this.currentIndex] as User;
      if (user.id) {
        this.destroyUser(user.id);
      }
    },
    async changePage(page: number) {
      this.currentPage = page;
      this.offset = (page - 1) * this.limit;
      this.loadingPage = true;
      const params = {
        limit: this.limit,
        offset: this.offset,
      };
      await this.listUsers(params);
      this.loadingPage = false;
    },
    fmt,
  },
  computed: {
    ...mapState(useUserStore, ["users"]),
    paging() {
      return getPaginationRange(
        Math.floor(this.resultsCount / this.limit) + 1,
        this.currentPage,
        1
      );
    },
  },
  async mounted() {
    const params = {
      limit: this.limit,
      offset: this.offset,
    };
    const response = await this.listUsers(params);
    this.resultsCount = response.data.count;
  },
});
</script>

<style lang="scss" scoped></style>
