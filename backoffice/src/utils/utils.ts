import { fmtCur } from "@/utils/currency";
import { fmtDate } from "@/utils/date";
import { fmt } from "@/utils/string";
import _ from "lodash";

const getPaginationRange = (
  totalPage: number,
  page: number,
  siblings: number
) => {
  const totalPageInArray = 7 + siblings;
  if (totalPageInArray >= totalPage) {
    return _.range(1, totalPage + 1);
  }

  const leftSiblingIndex = Math.max(page - siblings, 1);
  const showLeftDots = leftSiblingIndex > 2;

  const rightSiblingIndex = Math.min(page + siblings, totalPage);
  const showRightDots = rightSiblingIndex < totalPage - 2;

  if (!showLeftDots && showRightDots) {
    const leftItemsCount = 3 + 2 * siblings;
    const leftRange = _.range(1, leftItemsCount + 1);
    return [...leftRange, " ...", totalPage];
  } else if (showLeftDots && !showRightDots) {
    const rightItemsCount = 3 + 2 * siblings;
    const rightRange = _.range(totalPage - rightItemsCount + 1, totalPage + 1);
    return [1, "... ", ...rightRange];
  } else {
    const middleRange = _.range(leftSiblingIndex, rightSiblingIndex + 1);
    return [1, "... ", ...middleRange, " ...", totalPage];
  }
};

export { getPaginationRange, fmt, fmtCur, fmtDate };
