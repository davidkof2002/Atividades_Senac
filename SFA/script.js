// // Sistema de Filas de Atendimento - Logic
// let currentUser = null;
// let queue = [];
// let nextTicketNum = 1;
// let users = {}; // {email: {name, id?}}

// const STORAGE_KEY = 'filaAtendimentoData';

// // Init
// function init() {
//     loadData();
//     renderQueue();
// }

// // Load from localStorage
// function loadData() {
//     const data = localStorage.getItem(STORAGE_KEY);
//     if (data) {
//         const parsed = JSON.parse(data);
//         queue = parsed.queue || [];
//         nextTicketNum = parsed.nextTicketNum || 1;
//         users = parsed.users || {};
//     }
// }

// // Save to localStorage
// function saveData() {
//     localStorage.setItem(STORAGE_KEY, JSON.stringify({
//         queue,
//         nextTicketNum,
//         users
//     }));
// }

// // Register/Login
// function registerLogin() {
//     const name = document.getElementById('username').value.trim();
//     const email = document.getElementById('email').value.trim().toLowerCase();
//     if (!name || !email) {
//         alert('Preencha nome e email!');
//         return;
//     }
//     if (!users[email]) {
//         users[email] = {name};
//     }
//     currentUser = {name, email};
//     document.getElementById('loginSection').style.display = 'none';
//     document.getElementById('roleSection').style.display = 'block';
// }

// // Select Role
// function selectRole() {
//     const role = document.getElementById('roleSelect').value;
//     document.getElementById('roleSection').style.display = 'none';
//     if (role === 'paciente') {
//         document.getElementById('pacienteView').style.display = 'block';
//         document.getElementById('currentUser').textContent = currentUser.name;
//         updateMyStatus();
//     } else {
//         document.getElementById('atendenteView').style.display = 'block';
//         renderQueue();
//     }
// }

// // Update my status (for patient)
// function updateMyStatus() {
//     const userInQueue = queue.find(p => p.email === currentUser.email);
//     if (userInQueue) {
//         document.getElementById('myStatus').textContent = getStateText(userInQueue.state);
//         document.getElementById('myTicket').textContent = userInQueue.ticket;
//         document.getElementById('joinBtn').style.display = userInQueue.state !== 'waiting' ? 'none' : 'inline-block';
//     } else {
//         document.getElementById('myStatus').textContent = 'Não está na fila';
//         document.getElementById('myTicket').textContent = '';
//         document.getElementById('joinBtn').style.display = 'inline-block';
//     }
// }

// // Join Queue
// function joinQueue() {
//     const existing = queue.find(p => p.email === currentUser.email);
//     if (existing && existing.state !== 'done') {
//         alert('Você já está na fila!');
//         return;
//     }
    
//     // New or rejoin
//     const ticket = nextTicketNum.toString().padStart(3, '0');
//     const newPatient = {
//         id: Date.now(),
//         name: currentUser.name,
//         email: currentUser.email,
//         state: 'waiting',
//         ticket,
//         position: queue.filter(p => p.state === 'waiting').length + 1
//     };
    
//     if (existing) {
//         // Update existing if done
//         const idx = queue.findIndex(p => p.email === currentUser.email);
//         queue[idx] = newPatient;
//     } else {
//         queue.push(newPatient);
//     }
    
//     nextTicketNum++;
//     saveData();
//     updateMyStatus();
//     if (document.getElementById('atendenteView').style.display === 'block') {
//         renderQueue();
//     }
//     alert(`Senha ${ticket} gerada! Aguarde chamada.`);
// }

// // Call Next (Attendant)
// function callNext() {
//     const waiting = queue.find(p => p.state === 'waiting');
//     if (!waiting) {
//         alert('Fila vazia!');
//         return;
//     }
//     waiting.state = 'serving';
//     saveData();
//     renderQueue();
//     updateAllPatients();
//     alert(`Chamado: ${waiting.name} - Senha ${waiting.ticket}`);
// }

// // Finish Current
// function finishCurrent() {
//     const serving = queue.find(p => p.state === 'serving');
//     if (!serving) {
//         alert('Nenhum em atendimento!');
//         return;
//     }
//     serving.state = 'done';
//     saveData();
//     renderQueue();
//     updateAllPatients();
//     alert(`Finalizado: ${serving.name}`);
// }

// // Clear Queue
// function clearQueue() {
//     if (!confirm('Limpar toda a fila?')) return;
//     queue = queue.filter(p => p.state === 'done');
//     saveData();
//     renderQueue();
//     updateAllPatients();
// }

// // Render Queue Table
// function renderQueue() {
//     const tbody = document.querySelector('#queueTable tbody');
//     tbody.innerHTML = '';
//     queue.forEach(patient => {
//         const row = tbody.insertRow();
//         row.innerHTML = `
//             <td>${patient.ticket}</td>
//             <td>${patient.name}</td>
//             <td>${patient.email}</td>
//             <td><span class="state-${patient.state}">${getStateText(patient.state)}</span></td>
//             <td>${getCurrentPosition(patient)}</td>
//         `;
//     });
// }

// // Update all patients statuses (if views open)
// function updateAllPatients() {
//     if (currentUser && document.getElementById('pacienteView').style.display === 'block') {
//         updateMyStatus();
//     }
// }

// // Get current position (dynamic: count waiting before this)
// function getCurrentPosition(patient) {
//     const beforeWaiting = queue.slice(0, queue.indexOf(patient)).filter(p => p.state === 'waiting').length;
//     return patient.state === 'waiting' ? beforeWaiting + 1 : '-';
// }

// // Get state text
// function getStateText(state) {
//     const states = {
//         waiting: 'Aguardando atendimento',
//         serving: 'Em atendimento',
//         done: 'Atendimento finalizado'
//     };
//     return states[state] || state;
// }

// // Logout
// function logout() {
//     currentUser = null;
//     document.getElementById('loginSection').style.display = 'block';
//     document.getElementById('roleSection').style.display = 'none';
//     document.getElementById('pacienteView').style.display = 'none';
//     document.getElementById('atendenteView').style.display = 'none';
//     document.getElementById('username').value = '';
//     document.getElementById('email').value = '';
// }

// // Init on load
// window.onload = init;
