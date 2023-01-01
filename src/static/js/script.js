function enableDragSort(listClass) {
    const sortableLists = document.getElementsByClassName(listClass);
    Array.prototype.map.call(sortableLists, (list) => { enableDragList(list) });
}

function enableDragList(list) { Array.prototype.map.call(list.children, (item) => { enableDragItem(item) }); }

function enableDragItem(item) {
    item.setAttribute('draggable', true)
    item.ondrag = handleDrag;
    item.ondragend = handleDrop;
}

function handleDrag(item) {
    const selectedItem = item.target,
        list = selectedItem.parentNode,
        x = item.clientX,
        y = item.clientY;

    selectedItem.parentNode.classList.add('parent-drag-active');
    selectedItem.classList.add('drag-sort-active');
    let swapItem = document.elementFromPoint(x, y) === null ? selectedItem : document.elementFromPoint(x, y).closest("li");

    if (list === swapItem.parentNode) {

        swapItem = swapItem !== selectedItem.nextSibling ? swapItem : swapItem.nextSibling;
        list.insertBefore(selectedItem, swapItem);
    }
}

function handleDrop(item) {
    item.target.parentNode.classList.remove('parent-drag-active');
    item.target.classList.remove('drag-sort-active');

}

(() => { enableDragSort('drag-sort-enable') })();