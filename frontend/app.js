let editandoId = null;

// Elementos DOM
const loadingElement = document.getElementById('loading');
const errorElement = document.getElementById('error');
const vendasContainer = document.getElementById('vendasContainer');
const vendaForm = document.getElementById('vendaForm');

// Funções de utilidade
function showLoading() {
  loadingElement.style.display = 'block';
}

function hideLoading() {
  loadingElement.style.display = 'none';
}

function showError(message) {
  errorElement.textContent = message;
  errorElement.style.display = 'block';
  setTimeout(() => errorElement.style.display = 'none', 5000);
}

// Funções principais
async function carregarVendas() {
  showLoading();
  try {
    const res = await fetch('http://localhost:8000/vendas/');
    if (!res.ok) {
      throw new Error(`Erro ${res.status}: ${res.statusText}`);
    }
    const vendas = await res.json();
    renderizarVendas(vendas);
  } catch (error) {
    showError("Falha ao carregar vendas: " + error.message);
    console.error(error);
  } finally {
    hideLoading();
  }
}

function renderizarVendas(vendas) {
  vendasContainer.innerHTML = '';
  
  vendas.forEach(venda => {
    const div = document.createElement('div');
    div.className = 'venda-card';
    div.innerHTML = `
      <strong>${venda.Produto}</strong> - ${venda.Cliente} (${venda.Cidade})<br>
      Data: ${formatarData(venda["Data da Venda"])}<br>
      Quantidade: ${venda.Quantidade} | Preço Unitário: R$${venda["Preço Unitário"].toFixed(2)}<br>
      Valor Total: R$${venda["Valor Total"].toFixed(2)}<br>
      Vendedor: ${venda.Vendedor}<br>
      ID: ${venda.id}<br>
      <button onclick="preencherFormulario('${encodeURIComponent(JSON.stringify(venda))}')">Alterar</button>
      <button onclick="deletarVenda(${venda.id})">Remover</button>
    `;
    vendasContainer.appendChild(div);
  });
}

function formatarData(dataString) {
  const options = { day: '2-digit', month: '2-digit', year: 'numeric' };
  return new Date(dataString).toLocaleDateString('pt-BR', options);
}

// Manipulação do formulário
vendaForm.onsubmit = async function(e) {
  e.preventDefault();
  showLoading();
  
  const formData = new FormData(e.target);
  const payload = {
    data_da_venda: formData.get('data_da_venda'),
    cliente: formData.get('cliente'),
    produto: formData.get('produto'),
    quantidade: parseInt(formData.get('quantidade')),
    preco_unitario: parseFloat(formData.get('preco_unitario')),
    valor_total: parseFloat(formData.get('valor_total')),
    cidade: formData.get('cidade'),
    vendedor: formData.get('vendedor')
  };

  try {
    let response;
    if (editandoId) {
      response = await fetch(`http://localhost:8000/atualizar_venda/${editandoId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
    } else {
      response = await fetch('http://localhost:8000/Nova_Venda/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
    }

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Erro ao processar requisição');
    }

    resetarFormulario();
    await carregarVendas();
  } catch (error) {
    showError("Erro: " + error.message);
    console.error(error);
  } finally {
    hideLoading();
  }
};

function preencherFormulario(vendaJson) {
  const venda = JSON.parse(decodeURIComponent(vendaJson));
  editandoId = venda.id;
  
  // Formata a data para o input type="date" (YYYY-MM-DD)
  const dataVenda = new Date(venda["Data da Venda"]);
  const dataFormatada = dataVenda.toISOString().split('T')[0];
  
  document.getElementById('vendaId').value = venda.id;
  document.querySelector('[name="data_da_venda"]').value = dataFormatada;
  document.querySelector('[name="cliente"]').value = venda.Cliente;
  document.querySelector('[name="produto"]').value = venda.Produto;
  document.querySelector('[name="quantidade"]').value = venda.Quantidade;
  document.querySelector('[name="preco_unitario"]').value = venda["Preço Unitário"];
  document.querySelector('[name="valor_total"]').value = venda["Valor Total"];
  document.querySelector('[name="cidade"]').value = venda.Cidade;
  document.querySelector('[name="vendedor"]').value = venda.Vendedor;
  
  document.getElementById('btnSalvar').textContent = "Atualizar Venda";
}

function resetarFormulario() {
  editandoId = null;
  vendaForm.reset();
  document.getElementById('btnSalvar').textContent = "Criar Venda";
}

async function deletarVenda(id) {
  if (!confirm("Tem certeza que deseja remover esta venda?")) return;
  
  showLoading();
  try {
    const response = await fetch(`http://localhost:8000/deletar_venda/${id}`, { 
      method: 'DELETE' 
    });
    
    if (!response.ok) {
      throw new Error('Falha ao deletar venda');
    }
    
    await carregarVendas();
  } catch (error) {
    showError("Erro ao deletar: " + error.message);
    console.error(error);
  } finally {
    hideLoading();
  }
}

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
  carregarVendas();
});