---
url: https://shiptypes.com/
titel: "Ship types , not docs"
datum: 2026-10-11
datum_unsicher: true
erfasst: 2026-10-11
typ: url
quelle: url
status: verarbeitet
verarbeitet_am: 2026-10-11
source_notiz: 80_Knowledge/Sources/2026-10-11-shiptypes-ship-types-not-docs.md
medien: "1/1 lokal"
---

# Ship types , not docs

> Automatisch per `python ai.py ingest` erfasst. Quelle: [https://shiptypes.com/](https://shiptypes.com/)

## Inhalt

## Ship types , not docs

Types are the contract between services, docs are not

You know the drill: you need to integrate with a service, you find the documentation, you copy the example payload, you run it. 400 Bad Request.

You read the docs again, userId is marked optional, you try without it. 400 Bad Request. You search Slack, someone mentions a required header that isn't in the docs, you add it. 422 Unprocessable Entity. You DM the team that owns the service, they're in a different timezone. You wait.

Four hours later, you learn the docs were written for v2.1 and the service is on v2.8 . The field names changed. The error codes changed. Nobody updated the docs because nobody ever updates the docs.

The answer isn't better documentation. It's to stop writing documentation for contracts entirely. Ship types instead.

This matters more now than ever. AI agents are becoming your biggest API consumers, and they can't always DM other teams. If you want to be productive with AI, if you want your codebase to be a place where agents can actually work, you need to think of your codebase as an application that the agent is interacting with. Types are the UX of that application.

When you ship types instead of docs, developers hover over function calls and see the types. AI agents read your schemas and generate valid code on the first try. Partner integrations start with npm install @yourcompany/sdk . If it compiles, it works. No docs to read, no Slack threads to dig through, no 3am surprises.

### The Drift Is Inevitable

Here's the thing about documentation: it's a lossy copy.

You have the truth (your code), and then you have a human-written description of that truth (your docs). Every time you update the code, someone has to remember to update the description. They won't. Not because they're lazy, but because they're shipping features, fixing bugs, responding to incidents. Documentation updates don't page anyone at 3am.

The problem isn't discipline. The problem is that documentation and code are two separate artifacts that can diverge . Any system where two things must stay in sync manually will eventually fall out of sync. This is a law of nature, not a failure of process.

The point is not "never write documentation." Types tell you what : the shape of requests and responses, the valid values, the required fields. You still write prose for why a system exists, when to use it, and how it fits into the bigger picture. AI can take care of this. But the contract itself should never be prose. That's what types are for.

### Types Are Executable Documentation

A type definition is not just documentation. It is an executable contract that both producer and consumer must obey. It cannot drift because it is the code.

This insight came from building APIs at Cloudflare on the Developer Platform, and seeing how we do service-to-service communication.

With traditional HTTP APIs, you have this:

```
// Server defines an endpoint
app.post('/api/orders', handler);

// Client guesses at the contract
const response = await fetch('/api/orders', {
  method: 'POST',
  body: JSON.stringify({
    customerId: 'cust_123',  // or is it customer_id?
    items: [...]             // what shape are items?
  })
});
```

The client is flying blind. It's constructing a payload based on documentation, hope, and whatever worked last time. If the server changes, the client finds out at runtime. Usually in production. Usually at 2am.

Instead, we use Javascript-native Remote-procedure call (RPC) to communicate between services. It brings a ton of advantages, but today we're focusing on how it enforces the contract between services at transpilation-time.

### How I use JS-RPC

With Cloudflare JavaScript-native RPC, I directly invoke methods from one service in another service, with type-safety inferred from schemas.

```
// Service A defines its interface with types
export const CreateOrderSchema = z.object({
  customerId: z.string(),
  items: z.array(z.object({ productId: z.string(), quantity: z.number().int().positive() })).min(1),
  couponCode: z.string().optional(),
});

export const OrderSchema = CreateOrderSchema.extend({
  id: z.string(),
  status: z.enum(['pending', 'confirmed', 'shipped', 'delivered']),
  createdAt: z.string().datetime(),
  total: z.number(),
});

// Types derived from schemas - always in sync
export type CreateOrder = z.infer<typeof CreateOrderSchema>;
export type Order = z.infer<typeof OrderSchema>;

export class OrderService extends WorkerEntrypoint {
  async createOrder(request: CreateOrderRequest): Promise<Order> {
    // implementation
  }
}
```

```
// Service B calls it like a function
import type ORDER_SERVICE from "../service_a/index.ts";
interface Bindings {
  ORDER_SERVICE: Service<ORDER_SERVICE>;
} 

const order = await env.ORDER_SERVICE.createOrder({
  customerId: 'cust_123',
  items: [{ productId: 'prod_456', quantity: 2 }]
});
```

There's no documentation to read. There's no payload to guess at. Your IDE shows you exactly what CreateOrder type contains. The TypeScript compiler rejects invalid calls before you even run the code.

> The type signature is the documentation. It cannot drift because it is the code.

This enables coding agents to work through my codebase faster, and I have more confidence in their output. When an agent works in a codebase with RPC and shared types, it doesn't need to guess at payload shapes or parse documentation. It sees the function signature, gets autocomplete from the type system, and writes correct calls on the first try. The types become the contract between the agent and the codebase, the same way they're the contract between your services.

### The Schema Is the Source of Truth

Here's the pattern that makes this work:

```
graph TD
    Schema[Zod Schemawrite once] --> Backend[Backend Validation]
    Schema --> Frontend[Frontend Types]
    Schema --> OpenAPI[OpenAPI Spec]
    Schema --> Docs[Docs Site]
    Schema --> Mock[Mock Server]
    style Schema fill:#d1fae5,stroke:#059669,color:#065f46
    style Backend fill:#ede9fe,stroke:#7c3aed,color:#5b21b6
    style Frontend fill:#dbeafe,stroke:#3b82f6,color:#1e40af
    style OpenAPI fill:#fef3c7,stroke:#d97706,color:#92400e
    style Docs fill:#fee2e2,stroke:#f87171,color:#991b1b
    style Mock fill:#f3e8ff,stroke:#a855f7,color:#6b21a8
```

You define your contract once, in a schema language that can be validated at runtime (like Zod ). Everything else, TypeScript types, OpenAPI specs, documentation, SDKs, is generated from that schema.

When you change the schema, everything updates. Not eventually. Not when someone remembers. Automatically, in CI.

This is the key insight: the compiler becomes your documentation reviewer . You can't ship code that violates the contract because the contract is enforced by the type system.

### Every Surface Area, Typed

Once you internalize this, you start seeing untyped boundaries everywhere, and wanting to fix them.

Internal services : Your microservices calling each other over HTTP? That's an untyped boundary. Use RPC or shared schema packages.

Web clients : Your React app fetching from your API? Generate TypeScript types from your backend schemas. Libraries like tRPC or generated clients from OpenAPI make this trivial.

Mobile apps : Your iOS and Android apps? Generate Swift and Kotlin types from the same source schema. Same truth, different languages.

CLI tools : Your internal developer tools? Import the types directly. No excuse for CLIs to guess at API shapes.

External APIs : Your customers integrating with you? Ship SDKs, not documentation. If they have to read prose to understand your API, you've already failed.

### Make Your Codebase AI-Native

AI agents are becoming your biggest API consumers.

A well-configured agent can work without types. Agents are designed to fail and recover. They make an API call, get a 400, read the error, and try again. That's the feedback loop working as intended. But, an agent with types gets it right on the first call. An agent with only docs gets there in three or four attempts. Both "work," but one costs 4x the tokens, 4x the latency, and 4x the chances of a subtle error slipping through.

Think of your codebase as an application that the agent is interacting with. Types are the UX of that application. A codebase with strong types is a well-designed app, the agent can navigate it efficiently, understand the constraints, and produce correct code. A codebase with only prose documentation is a confusing app with no affordances, the agent can stumble through it, but it'll be slow and error-prone.

I've watched coding agents hallucinate API fields that don't exist, invent request formats based on vibes, and produce code that looks plausible but fails at runtime. They eventually recover through trial and error, but that's expensive. Give them types and they nail it immediately.

### A Practical Pattern

Enough theory. Here's how to actually do this.

#### Step 1: Define Your Schemas

```
// schemas/order.ts
import { z } from 'zod';

export const AddressSchema = z.object({
  street: z.string(),
  city: z.string(),
  country: z.string(),
  postalCode: z.string(),
});

export const OrderItemSchema = z.object({
  productId: z.string(),
  quantity: z.number().int().positive(),
  priceOverride: z.number().optional(), // Only for admin users
});

export const CreateOrderSchema = z.object({
  customerId: z.string(),
  items: z.array(OrderItemSchema).min(1),
  shippingAddress: AddressSchema,
  billingAddress: AddressSchema.optional(), // Defaults to shipping
  couponCode: z.string().optional(),
});

export const OrderSchema = CreateOrderSchema.extend({
  id: z.string(),
  status: z.enum(['pending', 'confirmed', 'shipped', 'delivered']),
  createdAt: z.string().datetime(),
  total: z.number(),
});

// Types derived from schemas - always in sync
export type CreateOrder = z.infer<typeof CreateOrderSchema>;
export type Order = z.infer<typeof OrderSchema>;
```

#### Step 2: Use Schemas for Validation

```
// api/orders.ts
import { CreateOrderSchema } from '../schemas/order';

app.post('/orders', async (req, res) => {
  const result = CreateOrderSchema.safeParse(req.body);

  if (!result.success) {
    // Zod gives you structured errors, not just "bad request"
    return res.status(400).json({
      error: 'Validation failed',
      issues: result.error.issues
    });
  }

  // result.data is typed as CreateOrder
  const order = await orderService.create(result.data);
  return res.json(order);
});
```

#### Step 3: Use RPC for Service-to-Service Communication

Instead of HTTP endpoints where clients guess at payloads, use RPC so the type signature is the contract.

On Cloudflare Workers , use JavaScript-native RPC . Your services call each other like local functions, with types enforced at the boundary:

```
// order-service/src/index.ts
import { WorkerEntrypoint } from 'cloudflare:workers';
import { CreateOrderSchema, type CreateOrder, type Order } from '../schemas/order';

export class OrderService extends WorkerEntrypoint {
  async createOrder(input: CreateOrder): Promise<Order> {
    const validated = CreateOrderSchema.parse(input);
    // ... create order
    return order;
  }
}

// checkout-service/src/index.ts - calls OrderService directly
import type OrderService from '../order-service/src/index';

interface Env {
  ORDER_SERVICE: Service<OrderService>;
}

export default {
  async fetch(req: Request, env: Env) {
    // Type-safe. No HTTP. No JSON. No docs to read.
    const order = await env.ORDER_SERVICE.createOrder({
      customerId: 'cust_123',
      items: [{ productId: 'prod_456', quantity: 2 }],
      shippingAddress: { street: '123 Main', city: 'SF', country: 'US', postalCode: '94102' },
    });
  }
}
```

Not on Cloudflare? The same principle applies with different tools:

- Any TypeScript backend : tRPC gives you end-to-end type safety between client and server with zero code generation

- Multi-language microservices : gRPC with Protocol Buffers generates typed clients for Go, Java, Python, Rust, and more

- AWS services : Smithy defines your API once and generates SDKs for every language

The key is the same regardless of tool: define the contract once, enforce it through types, eliminate the documentation layer .

#### Step 4: Generate SDKs and Docs

```
// scripts/generate.ts
import { zodToOpenAPI } from 'zod-to-openapi';
import { OrderSchema, CreateOrderSchema } from '../schemas/order';

// Generate OpenAPI spec
const openapi = zodToOpenAPI({
  schemas: { Order: OrderSchema, CreateOrder: CreateOrderSchema },
});
fs.writeFileSync('openapi.json', JSON.stringify(openapi));

// Generate SDKs from OpenAPI
execSync('npx openapi-typescript-codegen --input openapi.json --output sdk/typescript');
execSync('openapi-python-client generate --path openapi.json --output sdk/python');
```

#### Step 5: CI Enforces the Contract

```
# .github/workflows/api.yml
- name: Generate types
  run: npm run generate

- name: Check for uncommitted changes
  run: |
    if [[ -n $(git status --porcelain) ]]; then
      echo "Schema changed but generated files not committed!"
      exit 1
    fi

- name: Type check all consumers
  run: |
    npm run typecheck --workspace=frontend
    npm run typecheck --workspace=mobile
    npm run typecheck --workspace=cli
```

If someone changes the schema but forgets to regenerate the SDKs, CI fails. If someone changes the schema in a way that breaks a consumer, CI fails. The contract is enforced automatically.

### Common Objections

#### "I'd have to re-architect my entire system"

Nope, start at the boundaries that hurt most. Add schemas to your most-called endpoints and generate types from those. Wrap existing APIs with typed clients. Every new service starts schema-first. Legacy services get typed wrappers over time, you gradually replace untyped boundaries with typed ones.

#### "This only works for TypeScript shops"

The principle is language agnostic. Protocol Buffers generate types for Go, Java, Python, C++. Smithy generates for everything. JSON Schema can generate validators for any language. The insight is schema-first, not TypeScript-first.

#### "We generate types FROM our API, isn't that the same?"

No. Generating types from runtime behavior documents the mess; it doesn't prevent it. If your API returns inconsistent shapes, your generated types will be inconsistent. Schema-first means the schema is the authority, and the implementation must conform to it.

#### "Our API is too complex to type"

Then your API is too complex. The exercise of typing an API reveals accidental complexity. Fields that are "sometimes present". Responses that "depend on the request". Polymorphic payloads that could be anything. These are design problems, not typing problems. Fix the design.

#### "Can't AI just auto-generate the docs?"

Sure, and it probably will. But you're automating the maintenance of an artifact that shouldn't exist in the first place. If your types are the source of truth, what are the docs for ? The AI reads your code, extracts the contract, and writes it in prose so that... another AI can read the prose and reconstruct the contract? Just give it the types directly. AI-generated docs solve the maintenance problem but not the redundancy problem. You're keeping a lossy copy of your code up to date when consumers could just read the lossless original.

#### "Breaking changes are harder when types are shared"

That's the point. Breaking changes should be hard. They should require coordination. The current system doesn't prevent breaking changes, it just hides them until production. With shared types, you find out at build time, when you can still do something about it.

### The End State

When you fully commit to type-first APIs, something shifts.

New developers and AI agents don't ask "where are the docs?" They hover over function calls and see the types. They get autocomplete for valid fields. They see compile errors when they make mistakes.

Partner integrations don't start with "let me send you our documentation." They start with npm install @yourcompany/sdk or pip install yourcompany-client . The types guide them. If it compiles, it works.

AI agents don't hallucinate your API. They read the types, understand the constraints, and generate valid calls. The schema becomes the prompt.

Documentation still has value, but it should explain why an API works the way it does, not define what it accepts. Types are better suited for that. If correctness matters, the contract should be enforced by the compiler, not by a wiki page.

> If your API can be used incorrectly, it will be used incorrectly. Types make incorrect usage impossible.

I'm also building polylane.com , because nobody should be on-call in 2026.

## Bilder

![Boris Tane](medien/2026-10-11-shiptypes-ship-types-not-docs/01-bild.png)
