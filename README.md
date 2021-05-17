## ORIE 6590 Project: Inventory control with lead times and lost sales
### Authors: Wenchang Zhu and Zhi Liu

**Due to rendering issues with Github, we have included this same content in the PDF we handed in on Gradescope. Please feel free to check out that file instead.**

This document formally defines the lost-sales inventory optimization problem. In order to make it tractable, certain discretization measures were considered, making our model slightly different from the one introduced in Xin & Goldberg (2016) and in Lecture 5 of our class.

#### Model Setup

Let $\left\{D_{t}, t \geq 1\right\}$ be a sequence of independent and identically distributed (i.i.d.) demand realizations, distributed as the non-negative \textit{integer-valued} random variable (r.v.) $D$ with distribution $\mathcal{D}$, which we assume to have finite mean, and strictly positive variance. Let $L \geq 1$ be the deterministic lead time, and $h, p(>0)$ be the unit holding cost and lost-sales penalty, respectively.

In addition, let $I_{t}$ denote the on-hand inventory, and $\mathbf{x}_{t}=\left(x_{1, t}, \ldots, x_{L, t}\right)$ denote the pipeline vector of orders placed but not yet delivered, at the beginning of time period $t$, where $x_{i, t}$ is the order to be received in period $i+t-1$. Our state space consists of all the possible values of $(I_t,x_t)$. The ordered sequence of events in period $t$ is then as follows.

- A new amount of inventory $x_{1, t}$ is delivered and added to the on-hand inventory.
- A new order is placed.
- The demand $D_{t}$ is realized.
- Costs for period $t$ are incurred, and the on-hand inventory and pipeline vector are updated.
  


Note that the on-hand inventory is updated according to $I_{t+1}=\max \left(0, I_{t}+x_{1, t}-D_{t}\right)$, and the pipeline vector is updated such that (s.t.) $x_{1, t}$ is removed, $x_{i, t+1}$ is set equal to $x_{i+1, t}$ for $i \in[1, L-1]$, and $x_{L, t+1}$ is set equal to the new order placed. 

A policy $\pi$ consists of a sequence of measurable maps $\left\{f_{t}^{\pi}, t \geq 1\right\}$, where each $f_{t}^{\pi}$ is a function with domain $\mathbb{N}^{L+1}$ and range $\mathbb{N}$. In that case, for a given policy $\pi$, the order placed in period $t$ equals $f_{t}^{\pi}\left(\mathbf{x}_{t}, I_{t}\right)$. Note that the constraint on the domain and range of the policy function is introduced for tractability. Normally, they should be $\mathbb{R}^{+,L+1}$ and $\mathbb{R}^{+}$, as we will discuss in the next subsection.

We let $C_{t} \triangleq h\left(I_{t}+x_{1, t}-D_{t}\right)^{+}+p\left(I_{t}+x_{1, t}-D_{t}\right)^{-}$ denote the sum of the holding cost and lost-sales penalty in time period $t$, where $x^{+} \triangleq \max (x, 0), x^{-} \triangleq \max (-x, 0)$. 

As we will be interested in minimizing long-run average costs, and for simplicity, we suppose that the initial conditions are such that the initial inventory is 0 , and the initial pipeline vector is empty, i.e. $I_{1}=0, \mathbf{x}_{1}=\mathbf{0}$. 

For a given policy $\pi \in \Pi$, we let $C_{t}^{\pi}$ denote the corresponding cost incurred in period $t$, and 

$$
C(\pi) \triangleq \lim _{T \rightarrow \infty} \frac{1}{T} \mathbb{E}\left[\sum_{t=1}^{T}C_{t}^{\pi}\right]
$$
denote the long-run average cost incurred by $\pi$. Then the objective in this inventory control problem is simply
$$
\min_{\pi\in \Pi} C(\pi)
$$
where $\Pi$ denote the family of all admissible policies.

#### MDP Parameters

To conclude, we introduce our MDP parameters. For a discrete problem:

- State space: We suppose that there is a maximum inventory $I_{\max}$, and we can not order more than $I_{\max}$ at every time period. The state space keep track of the on-hand inventory and all the pending orders. The state space is $\mathcal{S}=\{0,1,\dots,I_{\max}\}^{L+1}$.
- Action space: At each period, the possible action is a new order $x_{L,t+1}$. The action space is $\mathcal{A}=\{0,1,\dots,I_{\max}\}$.
- Reward function: $r(I_t,x_t,a)=-h\left(I_{t}+x_{1, t}-D_{t}\right)^{+}-p\left(I_{t}+x_{1, t}-D_{t}\right)^{-}$.
- Transitions: From time $t$ to $t+1$, $I_{t+1}=\min\{I_{\max},\max \left(0, I_{t}+x_{1, t}-D_{t}\right)\}$, $x_{i,t+1}=x_{i+1,t}$, for $i=1,\dots,L-1$. $x_{L,t+1}$ is set to be the new action taken at this step. 

We also tried to formulate the problem in a continuous set up. In continuous setting, the state and action space would be $\mathcal{S}=\mathbb{R}_{+}^{L+1}$ and $\mathcal{R}=\mathbb{R}_{+}$, which are both uncountable. Transitions are $I_{t+1}=\max \left(0, I_{t}+x_{1, t}-D_{t}\right)$, $x_{i,t+1}=x_{i+1,t}$, for $i=1,\dots,L-1$. $x_{L,t+1}$ is set to be the new action taken at this step. Reward function remains the same.


#### Python Dependencies
