import type { NextApiRequest, NextApiResponse } from 'next';
import { MongoClient, ServerApiVersion } from 'mongodb';

const handler = async (req: NextApiRequest, res: NextApiResponse) => {
    console.log("API called");
    const uri = process.env.MONGODB_URI || "mongodb+srv://ADMIN:qwe123qwe123@cluster0.uspsoud.mongodb.net/?retryWrites=true&w=majority";
    const dbName = process.env.MONGODB_DB || 'Schedule_Optimization';

    if (!uri || !dbName) {
        res.status(500).json({ message: 'Environment variables MONGODB_URI and MONGODB_DB must be set' });
        return;
    }

    const client = new MongoClient(uri, {
        serverApi: {
            version: ServerApiVersion.v1,            
            strict: true,
            deprecationErrors: false
        }
    })

    try {
        console.log("Connecting...")
        await client.connect();
        console.log("Connected to MongoDB")
        const db = client.db(dbName);

        console.log("Connected to MongoDB");
        const data = await db.collection('ScheduleCollectionName').find({}).toArray();

        res.status(200).json(data);
    } catch (error : any) {
        res.status(500).json({ message: error.message });
    } finally {
        client.close();
    }
};

export default handler;
