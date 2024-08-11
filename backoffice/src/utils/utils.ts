import _ from "lodash";

const computePaging = (
  totalPages: number,
  totalPagesDisplay: number,
  page: number,
  siblings: number
) => {
  if (totalPages <= totalPagesDisplay) {
    return _.range(1, totalPages + 1);
  }

  const leftSiblingIndex = Math.max(page - siblings, 1);
  const showLeftDot = leftSiblingIndex > 3;

  const rightSiblingIndex = Math.min(page + siblings, totalPages);
  const showRightDot = rightSiblingIndex < totalPages - 2;

  if (!showLeftDot && showRightDot) {
    const leftRange = _.range(1, totalPagesDisplay - 1);
    return [...leftRange, " ...", totalPages];
  } else if (showLeftDot && !showRightDot) {
    const rigtRange = _.range(
      totalPages - (totalPagesDisplay - 2) + 1,
      totalPages + 1
    );
    return [1, "... ", ...rigtRange];
  } else {
    const middleRange = _.range(leftSiblingIndex, rightSiblingIndex + 1);
    return [1, "... ", ...middleRange, " ...", totalPages];
  }
};

export { computePaging };
