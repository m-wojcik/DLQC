import numpy as np
import jax.scipy as sp 

rho_x = np.array([[0,1],[1,0]])
rho_y = np.array([[0,-1j],[1j,0]])
rho_z = np.array([[1,0],[0,-1]])

rho_p = np.array([[0,1],[0,0]])
rho_m = np.array([[0,0],[1,0]])

psi_0 = np.array([1,0])
psi_1 = np.array([0,1])

def H(w, g):
    return w * rho_z + g * rho_x

def unitary_step(H, state, dt):
    U = sp.linalg.expm(-1j * H * dt)
    new_state = U @ state
    return new_state

def evolution(initial_state, ws, gs, nsteps, dt, return_measurements=False, return_fidelity=False, target=None):
    """The state is evolved unitarily over intervals of length dt with constant parameter values given by the tables ws, gs"""
    sigma_z = np.zeros(nsteps, dtype='complex')
    sigma_x = np.zeros(nsteps, dtype='complex')

    fidelities = np.zeros(nsteps)
    state = initial_state
    H_t0 = H(ws[0], gs[0])
    sigma_x[0] = np.dot(np.conj(state), rho_x @ state)
    sigma_z[0] = np.dot(np.conj(state), rho_z @ state)
    fidelity = np.abs(np.dot(np.conj(target), state))**2
    fidelities[0] = fidelity
    work = 0 
    for i in range(1,nsteps):
        state = unitary_step(H_t0, state, dt)
        sigma_x[i] = np.dot(np.conj(state), rho_x @ state)
        sigma_z[i] = np.dot(np.conj(state), rho_z @ state)
        fidelity = np.abs(np.dot(np.conj(target), state))**2
        fidelities[i] = fidelity
        H_t1 = H(ws[i], gs[i])
        dH = H_t1 - H_t0
        dU = np.dot(np.conj(state), dH @ state)
        work += dU # we identify work with the change of internal energy

        H_t0 = H_t1
        
    if return_measurements:
        return state, sigma_x, sigma_z, fidelities, work.real
    elif return_fidelity:
        return state, fidelity
    else:
        return state
    
    