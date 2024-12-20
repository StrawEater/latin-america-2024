---
marp: true
paginate: true
theme: gem5
title: Getting Started with gem5
author: Jason Lowe-Power
---

<!-- _class: title -->

## Welcome to the gem5 bootcamp!

---

## About the overall structure of the bootcamp

These slides and are available at <https://gem5bootcamp.github.io/latin-america-2024> for you to follow along.

(Note: They will be archived at <https://gem5bootcamp.github.io/latin-america-2024>)

The source for the slides, and what you'll be using throughout the bootcamp can be found on github at <https://github.com/gem5bootcamp/latin-america-2024>

> Note: Don't clone that repo, yet. We'll do that in a bit.

---

<!-- _class: two-col -->

## A bit about us

I am **Prof. Jason Lowe-Power** (he/him).
I am an associate professor in the Computer Science Department and
the *Project Management Committee chair* for the gem5 project.

I lead the Davis Computer Architecture Research (DArchR) Group.

<https://arch.cs.ucdavis.edu>

![UC Davis logo width:500px](00-introduction-to-bootcamp-imgs/expanded_logo_gold-blue.png)

![DArchR logo width:550px](00-introduction-to-bootcamp-imgs/darchr.png)

---

<!-- _class: two-col -->

## A bit about us

I am **Prof. Tamara Silbergleit Lehman** (she/her).
I am an assistant professor in the Electrical, Computer and Energy Engineering (ECEE) Department at the University of Colorado Boulder (CU Boulder).
Research Interests: Computer architecture security

Boulder Computer Architecture Research Lab (BCARL)
<https://www.colorado.edu/faculty/lehmantamara/>

![CU Boulder Logo w:450px center](00-introduction-to-bootcamp-imgs/Boulder%20centered.jpg)

> Note: interested in applying to the PhD program at CU Boulder? Ask me how to waive the application fee. Application deadline is **December 15th 2024**.

---

## Contributors to the bootcamp

![Everyone who has contributed to the bootcamp width:1200px](00-introduction-to-bootcamp-imgs/devs.drawio.svg)

---

<!-- _class: outline -->

## Plan for the week

### Day 1

- Introduction
  - [Computer architecture research intro](01-arch-research.md) <!-- 30 min (Tamara) -->
    - Introduction to computer architecture research
    - Example research idea: secure memory
    - Why do we need simulators?
  - [Background on simulation](01-simulation-background.md) <!-- 1 hour (Jason) -->
    - What is is simulation and why does it matter
    - gem5 history
  - [Getting started with gem5](02-getting-started.md) <!-- 10 minutes (Jason) -->
    - Getting into the codespace environment
    - Running your first simulation
    - **EXERCISE**: Run your first simulation <!-- 20 minutes -->
- Using gem5
  - [gem5's standard library](../02-Using-gem5/01-stdlib.md)
    - Quick overview of stdlib ideas (board, processor, cache hierarchy, memory) <!-- 15 minutes -->
    - **EXERCISE**: Building a simple Arm simulation <!-- 30 minutes -->
      - Outcome: Run a real workload in SE mode and look at stats
    - Quick overview of available components in stdlib
    - The idea of the simulator
      - Useful simulator functions (set_max_ticks/instructions)
  - [Modeling memory in gem5](../02-Using-gem5/06-memory.md)
    - Memory models in gem5 <!-- 15 minutes -->
  - [Traffic generators](../02-Using-gem5/12-traffic-generators.md)
    - Using traffic generator (Test board) <!-- 10 minutes -->
    - **EXERCISE**: Using the traffic generator to test memory <!-- 20 minutes -->
    - **EXERCISE**: Creating a new (hybrid) traffic generator <!-- 30 minutes -->
  - [Modeling caches in gem5](../02-Using-gem5/05-cache-hierarchies.md)
    - Cache models in gem5 (Ruby and classic) <!--  10 minutes -->
    - **EXERCISE**: 3 level classic cache hierarchy <!-- 30 minutes -->
    - 👉 Replacement policies
    - 👉 Tag policies
    - Tradeoffs between classic and Ruby <!-- 10 minutes -->
    - **HOMEWORK**: Example of using a Ruby hierarchy <!-- 30 minutes -->
    - Look at the gem5 generated statistics

### Day 2

- Using gem5
  - [Modeling cores in gem5](../02-Using-gem5/04-cores.md)
    - Types of CPU models in gem5 <!-- 15 minutes -->
    - **EXERCISE**: (Optional) Comparison of atomic and timing CPU <!-- 15 minutes -->
    - Look at the gem5 generated statistics
    - **EXERCISE**: Create a two custom out-of-order cores and compare <!-- 30 minutes -->
    - 👉 Branch predictors <!-- 15 minutes -->
    - 👉 Overview of ISAs and tradeoffs
  - [Running applications in gem5](../02-Using-gem5/03-running-in-gem5.md)
    - Intro to syscall emulation mode <!-- 30 minutes -->
    - The gem5-bridge utility and library
    - Cross compiling
    - **EXERCISE**: Create your own workload <!-- 30 minutes -->
  - [Using gem5 resources](../02-Using-gem5/02-gem5-resources.md)
    - Overview of resources, workloads, and suites <!-- 15 minutes -->
    - [Multisim](../02-Using-gem5/11-multisim.md) <!-- 10 minutes -->
    - **EXERCISE**: Running suite and seeing different results from different apps <!-- 30 minutes -->

**Now we have a full "baseline" that's running!**

### Day 3

- Developing gem5 models
  - [SimObject intro](../03-Developing-gem5-models/01-sim-objects-intro.md) <!-- (Mahyar) 0.5 hours -->
    - Development environment, code style, git branches
    - The most simple `SimObject`
    - Simple run script
    - How to add parameters to a `SimObject`
  - [Debugging and debug flags](../03-Developing-gem5-models/02-debugging-gem5.md) <!-- (Mahyar) 0.5 hours -->
    - How to enable debug flags (examples of DRAM and Exec)
    - `--debug-help`
    - Adding a new debug flag
    - Functions other than DPRINTF
    - Panic/fatal/assert
    - gdb?
  - [Event-driven simulation](../03-Developing-gem5-models/03-event-driven-sim.md) <!-- (Mahyar) 1 hours -->
    - Creating a simple callback event
    - Scheduling events
    - Modeling bandwidth and latency with events
    - Other SimObjects as parameters
    - Hello/Goodbye example with buffer
    - Clock domains?

### Day 4

- Using gem5 for research
  - Developing models to test secure memory

### Day 5

- Advanced running in gem5
  - [Full system simulation](../02-Using-gem5/07-full-system.md)
    - What is full system simulation? <!-- 30 minutes -->
    - Basics of booting up a real system in gem5
    - Running in FS mode
    - m5term to interact with a running system
    - "what do to when linux boots"
      - commands
    - Set kernel disk workload
    - Exit events
      - Simulation loop
      - Types of exit events
    - Creating disk images using packer and qemu <!-- **MAYBE SKIP** -->
    - Extending/modifying a gem5 disk image <!-- **MAYBE SKIP** -->
  - [Accelerating simulation](../02-Using-gem5/08-accelerating-simulation.md)
    - Switchable processor <!-- 15 minutes -->
    - KVM fast forwarding
    - 👉 **EXERCISE**: Running a simulation with KVM, switching, complex exits, and measuring <!-- 60 minutes -->
    - Checkpointing
    - 👉 **EXERCISE**: Running many different configs with checkpoint <!-- 30 minutes -->
  - [Sampled simulation with gem5](../02-Using-gem5/09-sampling.md)
    - Simpoint ideas <!-- 30 minutes -->
    - Simpoint analysis
    - Simpoint checkpoints
    - How to analyze sampled simulation data
    - **EXERCISE**: Running a simpoint simulation <!-- 60-90 minutes -->
    - Loopoint/Elfies <!-- 10 minutes -->
    - Statistical simulation ideas <!-- 10 minutes -->
    - **EXERCISE** Statistical simulation running and analysis
- **Putting it all together**
  - Running FS simulation with secure memory

###

### Extra stuff

- Advanced developing gem5 models
  - [Modeling Cores](../03-Developing-gem5-models/05-modeling-cores.md) <!-- (Bobby) 1.5 hours -->
    - New instructions
    - How the execution model works
    - Debugging
  - [Modeling cache coherence with Ruby and SLICC](../03-Developing-gem5-models/06-modeling-cache-coherence.md) <!--  (Jason) 1.5 hours -->
    - Ruby intro
    - Structure of SLICC
    - Building/running/configuring protocols
    - Debugging
    - Ruby network
    - (Note to Jason: could do a whole day here if split like before.)
  - [Extending gem5](../03-Developing-gem5-models/09-extending-gem5-models.md) <!-- (Zhantong) 1 hours -->
    - Probe points
    - Generic cache object
    - Base utilities (e.g., bitset)
    - Random numbers
    - Signal ports?
  - [Using the CHI protocol](../03-Developing-gem5-models/07-chi-protocol.md) <!-- (Jason) 0.5 hours -->
    - How is CHI different from other protocols?
    - Configuring a CHI hierarchy
  - [Modeling the on-chip network with Garnet](../03-Developing-gem5-models/08-ruby-network.md) <!-- (Jason) 1 hours -->
    - Garnet intro
    - Building/running/configuring networks
    - Debugging
  - [Ports and memory-based SimObjects](../03-Developing-gem5-models/04-ports.md) <!-- (Mahyar) 1 hours -->
    - Idea of ports (request/response), packets, interface
    - A simple memory object that forwards things
    - Connecting ports and writing config files
    - Adding stats to a SimObject
    - Adding latency and and modeling buffers/computing time
  - [Power modeling](../02-Using-gem5/10-modeling-power.md) <!-- 10 minutes -->
    - 👉 **EXERCISE**: Running a power simulation <!-- 15 minutes -->

---

## Our goals for the gem5 bootcamp

- Make gem5 less painful and flatten the learning curve
- Give you a vocabulary for asking questions​
- Provide a reference for the future​
- Give you material to take back and teach your colleagues

### Other likely outcomes

- You will be overwhelmed by the amount of information and how large gem5 is
  - That's OK! You can take these materials with you and refer back to them
- You will not understand everything
  - That's OK! You can ask questions as we go

---

## How this is going to work

- We'll be going mostly top-down
  1. How to use gem5
  2. How to each model can be used
  3. How to develop your own models and modify existing models
- Highly iterative:
  - You'll see the same thing over and over
  - Each time it will be one level deeper
- Lots of coding examples
  - Both live coding and practice problems

---

## Coding examples

You can write the following code

```python
print("Hello, world!")
print("You'll be seeing a lot of Python code")
print("The slides will be a reference, but we'll be doing a lot of live coding!")
```

And you'll see this output.

```console
Hello, world!
You'll be seeing a lot of Python code
The slides will be a reference, but we'll be doing a lot of live coding!
```

---

<!-- _class: exercise -->

## Exercises

Throughout the bootcamp, we'll have exercises for you to work on.

These exercises are designed to help you learn the material.

We will give you step-by-step instructions for each exercise.

### Questions

We will also have questions for you to answer?

---

## Slido

We'll be using Slido for questions and answers.

<iframe src="https://app.sli.do/event/qpr43XWrbjYJCdE3GHGCWg/embed/polls/428b4b2e-486e-47cb-be20-8bd2d5dd84a1" width="100%" height="440"></iframe>

---

## Bootcamp logistics

We'll be teaching each day from
9:00 a.m. - 12:00 p.m. and from 1:00 p.m. - 4:00 p.m.

We will be in the laboratories of pavilion 0+inf, but we'll be in different rooms each day.


| Día          | Laboratorio |
|--------------|-------------|
| Lunes 25/11  | Labo 1110   |
| Martes 26/11 | Labo 1111   |
| Miércoles 27/11 | Labo 1110 |
| Jueves 28/11 | Labo 1108   |
| Viernes 29/11 | Labo 1108  |

---

## Other admin things

---

## Important resources

### Bootcamp links

- [Bootcamp website](https://gem5bootcamp.github.io/latin-america-2024) (Maybe you're here now)
- [Source for bootcamp materials](https://github.com/gem5bootcamp/latin-america-2024) (You'll work here)
- [GitHub Classroom](https://classroom.github.com/a/zIM1ysn_) (Needed to use codespaces)

### gem5 links

- [gem5 code](https://github.com/gem5/gem5)
- [gem5 website](https://www.gem5.org/)
- [gem5 YouTube](https://youtube.com/@gem5)
- [gem5 Slack](https://gem5-workspace.slack.com/join/shared_invite/zt-2e2nfln38-xsIkN1aRmofRlAHOIkZaEA) (for asking offline questions)
