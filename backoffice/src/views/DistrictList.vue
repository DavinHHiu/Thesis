<template>
  <table class="w-full mt-[2rem] overflow-hidden">
    <thead>
      <tr>
        <th v-text="'Code'" />
        <th v-text="'Name'" />
        <th v-text="'Divistion type'" />
        <th v-text="'Codename'" />
        <th v-text="'Province code'" />
        <th v-text="'Status'" />
      </tr>
    </thead>
    <tbody>
      <template v-for="(district, index) in districts" :key="index">
        <tr :class="{ odd: !(index % 2) }">
          <td v-text="fmt(district.code)" />
          <td v-text="fmt(district.name)" />
          <td v-text="fmt(district.division_type)" />
          <td v-text="fmt(district.codename)" />
          <td v-text="fmt(district.province_code)" />
          <td v-text="fmt(district.is_active)" />
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
import TabLayout from "@/components/common/molecules/TabLayout.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useAddressStore } from "@/stores/address";
import { District } from "@/types/worker";
import { fmt } from "@/utils/string";
import { getPaginationRange } from "@/utils/utils";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "AddressView",
  components: {
    CustomButton,
    EllipsisDropdown,
    HeaderAction,
    Modal,
    PageTitle,
    PageBody,
    TabLayout,
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
  computed: {
    ...mapState(useAddressStore, ["districts"]),
    paging() {
      return getPaginationRange(
        Math.floor(this.resultsCount / this.limit) + 1,
        this.currentPage,
        1
      );
    },
  },
  methods: {
    ...mapActions(useAddressStore, ["listDistricts"]),
    handleActions(obj: any) {
      const district = this.districts[obj.currentIndex];
      if (obj.action === "update") {
        this.$router.push({
          name: "address.update",
          params: { id: district.code },
        });
      } else if (obj.action === "openModal") {
        const modal = this.$refs.deleteModal as InstanceType<typeof Modal>;
        modal.open();
      }
      this.currentIndex = obj.currentIndex;
    },
    async handleDelete() {
      const district = this.districts[this.currentIndex] as District;
      if (district.code) {
        this.destroyAddress(district.code);
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
      await this.listDistricts(params);
      this.loadingPage = false;
    },
    fmt,
  },
  async mounted() {
    const params = {
      limit: this.limit,
      offset: this.offset,
    };
    const response = await this.listDistricts(params);
    this.resultsCount = response.data.count;
  },
});
</script>
