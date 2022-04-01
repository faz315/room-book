function deleteRoom(roomId) {
  fetch("/delete-room", {
    method: "POST",
    body: JSON.stringify({ id: roomId }),
  }).then((_res) => {
    window.location.href = "/addroom";
  });
}

function deleteBooking(id) {
  fetch("/delete-booking", {
    method: "POST",
    body: JSON.stringify({ id: id }),
  }).then((_res) => {
    window.location.href = "/existingbooking";
  });
}
