"""Editorial cloud mappings. Local blocks stay local; services are not feature-equivalent."""
from html import escape as E
from textwrap import wrap
PROVIDERS={'aws':'AWS','gcp':'Google Cloud','azure':'Azure'}
def svc(name,url=None):return {'name':name,'url':url}
SERVICES={
'client':[svc('Client / device code')]*3,
'local':[svc('Local model runtime')]*3,
'policy':[svc('Application policy code')]*3,
'human':[svc('Human + review interface')]*3,
'app':[svc('AWS Lambda','https://docs.aws.amazon.com/lambda/latest/dg/welcome.html'),svc('Cloud Run','https://cloud.google.com/run/docs/overview/what-is-cloud-run'),svc('Azure Functions','https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview')],
'host':[svc('Amazon ECS on Fargate','https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html'),svc('Cloud Run','https://cloud.google.com/run/docs/overview/what-is-cloud-run'),svc('Azure Container Apps','https://learn.microsoft.com/en-us/azure/container-apps/overview')],
'llm':[svc('Amazon Bedrock','https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html'),svc('Gemini on Google Cloud','https://cloud.google.com/vertex-ai/generative-ai/docs/overview'),svc('Azure OpenAI','https://learn.microsoft.com/en-us/azure/ai-services/openai/overview')],
'agent':[svc('Amazon Bedrock Agents','https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html'),svc('Agent Platform Runtime','https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview'),svc('Microsoft Foundry Agent Service','https://learn.microsoft.com/en-us/azure/ai-services/agents/overview')],
'retrieval':[svc('Bedrock Knowledge Bases','https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html'),svc('Vector Search + app ACL checks','https://cloud.google.com/vertex-ai/docs/vector-search/overview'),svc('Azure AI Search','https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search')],
'predict':[svc('SageMaker AI custom endpoint','https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html'),svc('Google Cloud custom prediction','https://cloud.google.com/vertex-ai/docs/predictions/overview'),svc('Azure ML online endpoint','https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online')],
'stt':[svc('Amazon Transcribe','https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html'),svc('Cloud Speech-to-Text','https://cloud.google.com/speech-to-text/docs'),svc('Azure Speech: speech to text','https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text')],
'tts':[svc('Amazon Polly','https://docs.aws.amazon.com/polly/latest/dg/what-is.html'),svc('Cloud Text-to-Speech','https://cloud.google.com/text-to-speech/docs'),svc('Azure Speech: text to speech','https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech')],
'live':[svc('Amazon Nova Sonic on Bedrock','https://docs.aws.amazon.com/nova/latest/userguide/speech-bidirection.html'),svc('Gemini Live API','https://cloud.google.com/vertex-ai/generative-ai/docs/live-api'),svc('Azure OpenAI Realtime API','https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/audio-real-time')],
'store':[svc('Amazon S3','https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html'),svc('Cloud Storage','https://cloud.google.com/storage/docs/introduction'),svc('Azure Blob Storage','https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction')],
'queue':[svc('Amazon SQS','https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html'),svc('Pub/Sub subscription','https://cloud.google.com/pubsub/docs/overview'),svc('Azure Service Bus queue','https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview')],
'event':[svc('Amazon EventBridge','https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html'),svc('Eventarc','https://cloud.google.com/eventarc/docs/overview'),svc('Azure Event Grid','https://learn.microsoft.com/en-us/azure/event-grid/overview')],
'stream':[svc('Kinesis Data Streams','https://docs.aws.amazon.com/streams/latest/dev/introduction.html'),svc('Pub/Sub','https://cloud.google.com/pubsub/docs/overview'),svc('Azure Event Hubs','https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about')],
'window':[svc('Managed Service for Apache Flink','https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html'),svc('Dataflow','https://cloud.google.com/dataflow/docs/overview'),svc('Azure Stream Analytics','https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction')],
'workflow':[svc('AWS Step Functions','https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html'),svc('Workflows','https://cloud.google.com/workflows/docs/overview'),svc('Azure Durable Functions','https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview')],
'batch':[svc('SageMaker AI Batch Transform','https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html'),svc('Google Cloud batch prediction','https://cloud.google.com/vertex-ai/docs/predictions/get-batch-predictions'),svc('Azure ML batch endpoints','https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-batch')],
'ocr':[svc('Amazon Textract','https://docs.aws.amazon.com/textract/latest/dg/what-is.html'),svc('Document AI','https://cloud.google.com/document-ai/docs/overview'),svc('Azure Document Intelligence','https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview')]
}
ROLES={
'request-response':['client','app','predict','app','client'],
'rag':['client','retrieval','predict','llm','client'],
'tool-agent':['app','agent','policy','app','app'],
'chained-voice':['client','stt','llm','tts','client'],
'realtime-voice':['client','host','live','host','client'],
'wake-word':['client','local','host','live','client'],
'on-device':['client','local','local','local','client'],
'hybrid':['client','local','policy','llm','client'],
'embedded-copilot':['client','app','llm','app','human'],
'computer-use':['client','host','llm','policy','client'],
'event-driven':['event','queue','host','app','app'],
'batch':['store','host','batch','app','store'],
'streaming':['stream','window','predict','policy','app'],
'recommendation':['store','retrieval','predict','app','client'],
'document':['store','ocr','llm','app','human'],
'routing':['client','app','llm','app','client'],
'workflow':['event','llm','app','workflow','human'],
'multi-agent':['client','agent','host','app','app'],
'review-loop':['app','llm','app','llm','human'],
'human-review':['llm','app','human','policy','app']}
NOTES={
'client':'Runs in the client or existing interface. No managed cloud service is required for this block.',
'local':'Execute on-device with a compatible local runtime. The selected cloud is not on this inference path.',
'policy':'Write deterministic authorization and decision rules. A model prediction cannot grant permission.',
'human':'Provide an authenticated review interface; record approval against the exact proposal. Human judgment remains necessary.',
'app':'The named service hosts application code; supply validation, adapters, and business logic yourself.',
'host':'Host custom workers or session logic; implement deadlines, cancellation, state, and recovery. This host is not itself a model.',
'llm':'Choose a supported model and validate its outputs. Capabilities, limits, and availability vary by model and region.',
'agent':'Configure tools, least-privilege permissions, stopping conditions, and state. A managed runtime does not design these policies for you.',
'retrieval':'Build ingestion and indexing; enforce document permissions before returning evidence. Managed retrieval does not automatically supply your application ACLs.',
'predict':'Deploy a task-specific model for scoring or ranking. The endpoint is a host, not a pretrained universal ranker.',
'stt':'Recognize speech; test noise, accents, vocabulary, and domain-specific entity accuracy.',
'tts':'Synthesize text and manage playback in the client. Cancel stale or interrupted output.',
'live':'Use a supported bidirectional audio model and implement application-side controls for tool execution.',
'store':'Version input or output objects and configure access, retention, and atomic publishing conventions.',
'queue':'Use idempotency, bounded retries, and dead-letter handling; delivery and ordering semantics differ by configuration.',
'event':'Configure a trusted event source, destination integration, schema checks, and invocation permissions.',
'stream':'Ingest events with suitable partitioning and retention. Stream ingestion does not itself run inference.',
'window':'Implement event-time windows, late-data behavior, and consistent feature calculations.',
'workflow':'Encode explicit stages, retries, and state transitions. Model calls and validation are distinct activities.',
'batch':'Shown for a supported custom prediction model; foundation models may require a different model-specific batch API.',
'ocr':'Select appropriate OCR, layout, or extraction processors. Preserve source-page evidence for review.'}
EXTRA={
'request-response':'A custom prediction endpoint is shown. For generative text, use Amazon Bedrock, Gemini on Google Cloud, or Azure OpenAI instead.',
'rag':'Also build ingestion: documents → parsing and chunks → embeddings → indexed store. Align embedding versions, enforce access filters, and consider a reranker only if evaluation justifies it.',
'embedded-copilot':'Retrieval is an optional branch alongside the model. Follow the RAG design for ingestion, grounding, and access filtering.',
'computer-use':'A cloud model cannot directly operate a user’s desktop. Add a permissioned local control bridge or an isolated remote environment, and verify compatibility of the execution host.',
'realtime-voice':'Input and output transport belong to one bidirectional session. Use a streaming-capable host; a short-lived function invocation is not an equivalent substitute.',
'wake-word':'The wake detector stays local. Activate the remote session only after a trigger and provide an explicit listening indicator.',
'on-device':'Every block stays local for all three selections. Cloud training and model distribution are optional separate paths, not requirements for offline inference.',
'hybrid':'If local processing succeeds, bypass the optional remote model. Only send allowed data when escalation is necessary.',
'event-driven':'The worker invokes a separate model API or prediction endpoint. Add the chosen provider’s model service to the worker and restrict its permissions.',
'recommendation':'Candidate retrieval can use vector search or a different index. A relevance scorer and business re-ranking policy remain separate responsibilities.',
'multi-agent':'Run specialists concurrently in separate sessions or workers. The host does not create the specialists; application code must assign scope, collect evidence, and reconcile conflicts.',
'workflow':'The workflow orchestrator controls the earlier stages as well; the diagram is a logical sequence, not a physical deployment order.',
'human-review':'Reject changed, expired, or replayed approvals. The final executor must recheck that the approved payload and permissions still match.',
'review-loop':'Evaluation can call another model, deterministic tests, or a person. A second model may share the generator’s errors; set a strict iteration budget.',
'routing':'The specialist block represents multiple configured paths; it may select different models, code, or workflows.',
'document':'The document processor may already extract some fields. Skip the language-model step when deterministic extraction is sufficient.'}
KINDS={'client':'actor','human':'actor','policy':'decision','store':'store','stream':'queue','queue':'queue','event':'event'}
LOOPS={'tool-agent':(4,1,'Continue or stop; enforce a step budget'),'review-loop':(3,1,'Revise until criteria pass or the budget is exhausted'),'computer-use':(4,1,'Observe the result before acting again'),'human-review':(3,0,'Rejected or changed proposal returns for revision')}
def choice(role,provider):return SERVICES[role][list(PROVIDERS).index(provider)]
def svg(item,provider):
 def text(x,y,value,size=14,fill='#25364c',anchor='start',bold=False,width=25):
  rows=wrap(value,width=width,break_long_words=False)
  return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{600 if bold else 400}">'+''.join(f'<tspan x="{x}" dy="{0 if j==0 else 18}">{E(t)}</tspan>' for j,t in enumerate(rows))+'</text>'
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="420" viewBox="0 0 1280 420" font-family="Arial, sans-serif" role="img" aria-labelledby="title desc"><title id="title">{E(item["title"])} — {PROVIDERS[provider]}</title><desc id="desc">{E(" → ".join(item["flow"]))}. Suggested services appear below each block.</desc><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="#60738b"/></marker></defs><rect width="1280" height="420" fill="white"/><rect x="12" y="48" width="1256" height="325" rx="5" fill="#fafbfd" stroke="#c5cfdd" stroke-dasharray="6 5"/>']
 parts.append(text(30,28,PROVIDERS[provider].upper()+' / REFERENCE FLOW',12,width=90,bold=True))
 parts.append(text(30,70,'Logical system scope — device, application, and cloud blocks may have different deployment boundaries.',12,width=130,fill='#52647a'))
 for i,(label,role) in enumerate(zip(item['flow'],ROLES[item['id']])):
  x=30+i*249;kind=KINDS.get(role,'process');color={'actor':'#edf2fa','decision':'#fff4d8','store':'#e8f4ed','queue':'#f0ebfa'}.get(kind,'#ecf4ff')
  if i<4:parts.append(f'<path d="M{x+224} 161H{x+243}" stroke="#60738b" stroke-width="1.5" marker-end="url(#arrow)"/>')
  if kind=='decision':parts.append(f'<path d="M{x+112} 95L{x+224} 161L{x+112} 227L{x} 161Z" fill="{color}" stroke="#aa903f"/>')
  else:
   parts.append(f'<rect x="{x}" y="103" width="224" height="116" rx="{28 if kind=="actor" else 4}" fill="{color}" stroke="#94a7be"/>')
   if kind=='store':parts.append(f'<ellipse cx="{x+112}" cy="103" rx="112" ry="11" fill="{color}" stroke="#94a7be"/>')
   if kind=='queue':
    for k in range(3):parts.append(f'<path d="M{x+8+k*6} 113V209" stroke="#b0a0c6"/>')
  parts.append(text(x+112,139,label,15,anchor='middle',bold=True,width=23))
  parts.append(text(x+112,201,f'{i+1:02d} · {kind.upper()}',10,anchor='middle'))
  selected=choice(role,provider)
  parts.append(text(x+6,256,selected['name'],14,fill='#174f9d',bold=True))
  parts.append(text(x+6,324,'LOCAL / CUSTOM' if role in ('client','local','policy','human') else 'SERVICE OPTION',10,fill='#60738b'))
 if item['id'] in LOOPS:
  start,end,label=LOOPS[item['id']];a=30+start*249;b=30+end*249
  parts.append(f'<path d="M{a+224} 185H{a+234}V350H{b-12}V180H{b}" fill="none" stroke="#60738b" stroke-dasharray="5 4" marker-end="url(#arrow)"/>')
  parts.append(text(30,398,label+' · dashed arrow = control / repeat path',12,width=150))
 elif item['id']=='hybrid':
  parts.append('<path d="M640 104V83H1138V98" fill="none" stroke="#60738b" stroke-dasharray="5 4" marker-end="url(#arrow)"/>')
  parts.append(text(30,398,'Local success bypasses remote inference. Solid arrows indicate the primary data / execution path.',12,width=150))
 else:parts.append(text(30,398,'Solid arrows = primary data / execution path. Blocks show responsibilities, not necessarily separate deployments.',12,width=150))
 return ''.join(parts)+'</svg>'
